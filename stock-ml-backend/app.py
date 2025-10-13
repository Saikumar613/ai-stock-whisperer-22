from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Supabase configuration
SUPABASE_URL = "https://scravbcqtsubczqkmlnm.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNjcmF2YmNxdHN1YmN6cWttbG5tIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MjQ4MTMsImV4cCI6MjA3NTAwMDgxM30.abpVVbWCWctlRgjonSdTklo5n2qB_mY-VpEGBvVOheM"

def save_to_database(table, data):
    """Save data to Supabase database"""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/{table}",
        headers=headers,
        json=data
    )
    return response.json()

@app.route('/api/get_stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Fetch stock data from Yahoo Finance and save to database"""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if hist.empty:
            return jsonify({"error": "No data found for symbol"}), 404
        
        # Save to database
        stock_data_records = []
        for date, row in hist.iterrows():
            stock_data_records.append({
                "symbol": symbol.upper(),
                "date": date.isoformat(),
                "open_price": float(row['Open']),
                "high_price": float(row['High']),
                "low_price": float(row['Low']),
                "close_price": float(row['Close']),
                "volume": int(row['Volume'])
            })
        
        # Save to database (batch insert)
        if stock_data_records:
            save_to_database("stock_data", stock_data_records)
        
        return jsonify({
            "symbol": symbol.upper(),
            "data": hist.reset_index().to_dict('records'),
            "current_price": float(hist['Close'].iloc[-1])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    """Run ML predictions and save to database"""
    try:
        data = request.get_json()
        symbol = data.get('symbol')
        user_id = data.get('user_id')
        model_type = data.get('model_type', 'RandomForest')
        
        if not symbol or not user_id:
            return jsonify({"error": "Symbol and user_id are required"}), 400
        
        # Fetch historical data
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if hist.empty:
            return jsonify({"error": "No data found"}), 404
        
        # Prepare data
        df = hist[['Close']].copy()
        df['Prediction'] = df['Close'].shift(-1)
        df = df.dropna()
        
        X = np.array(df.drop(['Prediction'], axis=1))
        y = np.array(df['Prediction'])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model based on type
        if model_type == 'SVM':
            model = SVR(kernel='rbf', C=1e3, gamma=0.1)
        elif model_type == 'DecisionTree':
            model = DecisionTreeRegressor(random_state=42)
        elif model_type == 'RandomForest':
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == 'LSTM':
            # LSTM implementation
            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled_data = scaler.fit_transform(X_train)
            
            model = Sequential()
            model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
            model.add(Dropout(0.2))
            model.add(LSTM(50, return_sequences=False))
            model.add(Dropout(0.2))
            model.add(Dense(25))
            model.add(Dense(1))
            
            model.compile(optimizer='adam', loss='mean_squared_error')
            X_train_reshaped = scaled_data.reshape((scaled_data.shape[0], scaled_data.shape[1], 1))
            model.fit(X_train_reshaped, y_train, batch_size=1, epochs=25, verbose=0)
            
            # Predict
            X_test_scaled = scaler.transform(X_test)
            X_test_reshaped = X_test_scaled.reshape((X_test_scaled.shape[0], X_test_scaled.shape[1], 1))
            prediction = model.predict(X_test_reshaped)
            predicted_price = float(prediction[0][0])
        else:
            return jsonify({"error": "Invalid model type"}), 400
        
        if model_type != 'LSTM':
            model.fit(X_train, y_train)
            prediction = model.predict(X_test)
            predicted_price = float(prediction[0])
        
        # Calculate confidence (simplified)
        confidence = float(model.score(X_test, y_test) * 100) if model_type != 'LSTM' else 85.0
        
        # Save prediction to database
        prediction_record = {
            "user_id": user_id,
            "symbol": symbol.upper(),
            "predicted_price": round(predicted_price, 2),
            "model_type": model_type,
            "confidence": round(confidence, 2)
        }
        
        save_to_database("stock_predictions", prediction_record)
        
        return jsonify({
            "symbol": symbol.upper(),
            "predicted_price": round(predicted_price, 2),
            "current_price": float(hist['Close'].iloc[-1]),
            "model_type": model_type,
            "confidence": round(confidence, 2)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
