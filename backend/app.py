# ============================================
# STOCK PREDICTION BACKEND WITH MONGODB
# ============================================
# Tool: Python 3.8+
# Run: python app.py
# Port: 5000
# ============================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# ============================================
# MONGODB CONNECTION
# ============================================

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/stock_prediction')

try:
    client = MongoClient(MONGODB_URI)
    db = client.get_database()
    
    # Collections
    stock_data_collection = db.stock_data
    stock_predictions_collection = db.stock_predictions
    
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {str(e)}")

# ============================================
# HELPER FUNCTIONS
# ============================================

def save_stock_data(symbol, data):
    """Save stock data to MongoDB"""
    try:
        stock_data_collection.insert_one({
            'symbol': symbol,
            'data': data,
            'created_at': datetime.now()
        })
        return True
    except Exception as e:
        print(f"Error saving stock data: {str(e)}")
        return False

def save_prediction(symbol, user_id, prediction_data):
    """Save prediction to MongoDB"""
    try:
        stock_predictions_collection.insert_one({
            'symbol': symbol,
            'user_id': user_id,
            'predicted_price': prediction_data['predicted_price'],
            'current_price': prediction_data['current_price'],
            'confidence': prediction_data['confidence'],
            'model_type': prediction_data['model_type'],
            'created_at': datetime.now()
        })
        return True
    except Exception as e:
        print(f"Error saving prediction: {str(e)}")
        return False

# ============================================
# API ENDPOINTS
# ============================================

@app.route('/api/get_stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """
    Fetch historical stock data from Yahoo Finance
    Example: GET /api/get_stock_data/AAPL
    """
    try:
        # Fetch data from Yahoo Finance
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if hist.empty:
            return jsonify({'error': 'Stock symbol not found'}), 404
        
        # Format data for frontend
        stock_data = {
            'symbol': symbol,
            'history': hist.reset_index().to_dict('records'),
            'current_price': float(hist['Close'].iloc[-1])
        }
        
        # Save to MongoDB
        save_stock_data(symbol, stock_data['history'])
        
        return jsonify(stock_data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Predict stock price using ML models
    
    Request Body:
    {
        "symbol": "AAPL",
        "user_id": "user123",
        "model_type": "RandomForest"  // Optional: SVM, DecisionTree, RandomForest, LSTM
    }
    """
    try:
        data = request.get_json()
        symbol = data.get('symbol')
        user_id = data.get('user_id', 'anonymous')
        model_type = data.get('model_type', 'RandomForest')
        
        if not symbol:
            return jsonify({'error': 'Symbol is required'}), 400
        
        # Fetch historical data
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if hist.empty:
            return jsonify({'error': 'Stock symbol not found'}), 404
        
        # Prepare data
        df = hist[['Close']].copy()
        df['Prediction'] = df['Close'].shift(-1)
        df = df.dropna()
        
        # Features and target
        X = np.array(df[['Close']])
        y = np.array(df['Prediction'])
        
        # Split data (80% train, 20% test)
        split = int(0.8 * len(X))
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]
        
        # Scale data
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Select and train model
        if model_type == 'SVM':
            model = SVR(kernel='rbf', C=1e3, gamma=0.1)
        elif model_type == 'DecisionTree':
            model = DecisionTreeRegressor(random_state=42)
        elif model_type == 'RandomForest':
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == 'LSTM':
            # For LSTM, use RandomForest as fallback (LSTM requires tensorflow)
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model_type = 'RandomForest'  # Update model type
        else:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        # Train model
        model.fit(X_train_scaled, y_train)
        
        # Make prediction for next day
        last_price = np.array([[hist['Close'].iloc[-1]]])
        last_price_scaled = scaler.transform(last_price)
        prediction = model.predict(last_price_scaled)[0]
        
        # Calculate confidence (simplified)
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        confidence = (train_score + test_score) / 2
        
        # Prepare result
        result = {
            'predicted_price': float(prediction),
            'current_price': float(hist['Close'].iloc[-1]),
            'confidence': float(confidence),
            'model_type': model_type,
            'symbol': symbol
        }
        
        # Save prediction to MongoDB
        save_prediction(symbol, user_id, result)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Check if the API is running"""
    return jsonify({'status': 'healthy', 'database': 'MongoDB'}), 200


# ============================================
# RUN THE APP
# ============================================

if __name__ == '__main__':
    print("🚀 Starting Flask Backend with MongoDB...")
    print("📊 Stock Prediction API is running!")
    print("🔗 Access at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
