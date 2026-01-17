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
import time
import concurrent.futures
from stock_symbols import STOCK_SYMBOLS, get_all_symbols, get_symbols_by_sector, search_stocks, get_all_sectors

app = Flask(__name__)
CORS(app)

# MongoDB configuration (local)
MONGODB_URI = "mongodb://localhost:27017/stockDB"

# Rate limiting settings for Yahoo Finance
MAX_CONCURRENT_REQUESTS = 5
REQUEST_DELAY = 0.5  # seconds between requests

def fetch_stock_data_safe(symbol, period="1y"):
    """Safely fetch stock data with error handling"""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None, f"No data found for {symbol}"
        
        # Get additional info
        try:
            info = stock.info
            company_name = info.get('longName', info.get('shortName', symbol))
            sector = info.get('sector', 'Unknown')
            market_cap = info.get('marketCap', 0)
            pe_ratio = info.get('trailingPE', None)
            dividend_yield = info.get('dividendYield', None)
        except:
            # Fallback to our database
            stock_info = STOCK_SYMBOLS.get(symbol.upper(), {})
            company_name = stock_info.get('name', symbol)
            sector = stock_info.get('sector', 'Unknown')
            market_cap = None
            pe_ratio = None
            dividend_yield = None
        
        return {
            "symbol": symbol.upper(),
            "company_name": company_name,
            "sector": sector,
            "market_cap": market_cap,
            "pe_ratio": pe_ratio,
            "dividend_yield": dividend_yield,
            "data": hist.reset_index().to_dict('records'),
            "current_price": float(hist['Close'].iloc[-1]),
            "open_price": float(hist['Open'].iloc[-1]),
            "high_price": float(hist['High'].iloc[-1]),
            "low_price": float(hist['Low'].iloc[-1]),
            "volume": int(hist['Volume'].iloc[-1]),
            "price_change": float(hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) if len(hist) > 1 else 0,
            "price_change_percent": float(((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100) if len(hist) > 1 else 0
        }, None
    except Exception as e:
        return None, str(e)


@app.route('/api/symbols', methods=['GET'])
def get_symbols():
    """Get all available stock symbols"""
    sector = request.args.get('sector')
    search_query = request.args.get('search')
    
    if search_query:
        results = search_stocks(search_query)
        return jsonify({
            "count": len(results),
            "symbols": results
        })
    elif sector:
        symbols = get_symbols_by_sector(sector)
        return jsonify({
            "sector": sector,
            "count": len(symbols),
            "symbols": {s: STOCK_SYMBOLS[s] for s in symbols}
        })
    else:
        return jsonify({
            "total_count": len(STOCK_SYMBOLS),
            "symbols": STOCK_SYMBOLS
        })


@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Get all available sectors"""
    sectors = get_all_sectors()
    sector_counts = {}
    for sector in sectors:
        sector_counts[sector] = len(get_symbols_by_sector(sector))
    
    return jsonify({
        "sectors": sectors,
        "sector_counts": sector_counts
    })


@app.route('/api/get_stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Fetch stock data from Yahoo Finance"""
    period = request.args.get('period', '1y')  # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, max
    
    data, error = fetch_stock_data_safe(symbol, period)
    
    if error:
        return jsonify({"error": error}), 404
    
    return jsonify(data)


@app.route('/api/get_multiple_stocks', methods=['POST'])
def get_multiple_stocks():
    """Fetch data for multiple stocks efficiently"""
    try:
        request_data = request.get_json()
        symbols = request_data.get('symbols', [])
        period = request_data.get('period', '1y')
        
        if not symbols:
            return jsonify({"error": "No symbols provided"}), 400
        
        # Limit to prevent abuse
        if len(symbols) > 50:
            symbols = symbols[:50]
        
        results = {}
        errors = {}
        
        # Use ThreadPoolExecutor for concurrent fetching
        def fetch_single(sym):
            time.sleep(REQUEST_DELAY)  # Rate limiting
            return sym, fetch_stock_data_safe(sym, period)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS) as executor:
            futures = {executor.submit(fetch_single, sym): sym for sym in symbols}
            
            for future in concurrent.futures.as_completed(futures):
                sym, (data, error) = future.result()
                if data:
                    results[sym] = data
                else:
                    errors[sym] = error
        
        return jsonify({
            "success_count": len(results),
            "error_count": len(errors),
            "data": results,
            "errors": errors
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/get_sector_stocks/<sector>', methods=['GET'])
def get_sector_stocks(sector):
    """Get live data for all stocks in a sector"""
    try:
        symbols = get_symbols_by_sector(sector)
        
        if not symbols:
            return jsonify({"error": f"No stocks found for sector: {sector}"}), 404
        
        # Limit to first 20 for performance
        symbols = symbols[:20]
        
        results = {}
        errors = {}
        
        for symbol in symbols:
            data, error = fetch_stock_data_safe(symbol, "1mo")
            time.sleep(REQUEST_DELAY)
            
            if data:
                results[symbol] = {
                    "company_name": data["company_name"],
                    "current_price": data["current_price"],
                    "price_change": data["price_change"],
                    "price_change_percent": data["price_change_percent"],
                    "volume": data["volume"]
                }
            else:
                errors[symbol] = error
        
        return jsonify({
            "sector": sector,
            "count": len(results),
            "stocks": results,
            "errors": errors if errors else None
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/market_overview', methods=['GET'])
def get_market_overview():
    """Get overview of major market indices and top stocks"""
    try:
        # Major indices
        indices = ["^GSPC", "^DJI", "^IXIC", "^RUT", "^VIX"]
        index_names = {
            "^GSPC": "S&P 500",
            "^DJI": "Dow Jones",
            "^IXIC": "NASDAQ",
            "^RUT": "Russell 2000",
            "^VIX": "VIX"
        }
        
        # Top stocks by market cap
        top_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "BRK-B", "JPM", "V"]
        
        index_data = {}
        stock_data = {}
        
        # Fetch index data
        for idx in indices:
            data, error = fetch_stock_data_safe(idx, "1d")
            if data:
                index_data[index_names.get(idx, idx)] = {
                    "current_price": data["current_price"],
                    "price_change": data["price_change"],
                    "price_change_percent": data["price_change_percent"]
                }
            time.sleep(REQUEST_DELAY)
        
        # Fetch top stocks data
        for symbol in top_stocks:
            data, error = fetch_stock_data_safe(symbol, "1d")
            if data:
                stock_data[symbol] = {
                    "company_name": data["company_name"],
                    "current_price": data["current_price"],
                    "price_change": data["price_change"],
                    "price_change_percent": data["price_change_percent"]
                }
            time.sleep(REQUEST_DELAY)
        
        return jsonify({
            "timestamp": datetime.now().isoformat(),
            "indices": index_data,
            "top_stocks": stock_data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/trending', methods=['GET'])
def get_trending():
    """Get trending/most active stocks"""
    try:
        # Popular tech stocks as trending
        trending_symbols = [
            "AAPL", "NVDA", "TSLA", "AMD", "META", 
            "GOOGL", "MSFT", "AMZN", "NFLX", "COIN",
            "PLTR", "SOFI", "NIO", "RIVN", "GME"
        ]
        
        trending_data = []
        
        for symbol in trending_symbols:
            data, error = fetch_stock_data_safe(symbol, "5d")
            if data:
                trending_data.append({
                    "symbol": symbol,
                    "company_name": data["company_name"],
                    "current_price": data["current_price"],
                    "price_change": data["price_change"],
                    "price_change_percent": data["price_change_percent"],
                    "volume": data["volume"]
                })
            time.sleep(REQUEST_DELAY)
        
        # Sort by absolute price change percentage
        trending_data.sort(key=lambda x: abs(x["price_change_percent"]), reverse=True)
        
        return jsonify({
            "count": len(trending_data),
            "trending": trending_data
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/search/<query>', methods=['GET'])
def search_stock(query):
    """Search for stocks by name or symbol"""
    results = search_stocks(query)
    
    # Enrich with live price data for top 10 results
    enriched_results = {}
    for i, (symbol, info) in enumerate(results.items()):
        if i >= 10:
            break
        
        data, error = fetch_stock_data_safe(symbol, "1d")
        if data:
            enriched_results[symbol] = {
                **info,
                "current_price": data["current_price"],
                "price_change_percent": data["price_change_percent"]
            }
        else:
            enriched_results[symbol] = info
        time.sleep(REQUEST_DELAY)
    
    return jsonify({
        "query": query,
        "count": len(results),
        "results": enriched_results
    })


@app.route('/api/predict', methods=['POST'])
def predict():
    """Run ML predictions"""
    try:
        data = request.get_json()
        symbol = data.get('symbol')
        user_id = data.get('user_id')
        model_type = data.get('model_type', 'RandomForest')
        
        if not symbol:
            return jsonify({"error": "Symbol is required"}), 400
        
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
        
        current_price = float(hist['Close'].iloc[-1])
        price_change = predicted_price - current_price
        price_change_percent = (price_change / current_price) * 100
        
        return jsonify({
            "symbol": symbol.upper(),
            "predicted_price": round(predicted_price, 2),
            "current_price": current_price,
            "price_change": round(price_change, 2),
            "price_change_percent": round(price_change_percent, 2),
            "model_type": model_type,
            "confidence": round(confidence, 2),
            "recommendation": "BUY" if price_change_percent > 2 else "SELL" if price_change_percent < -2 else "HOLD"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/compare', methods=['POST'])
def compare_stocks():
    """Compare multiple stocks"""
    try:
        data = request.get_json()
        symbols = data.get('symbols', [])
        period = data.get('period', '1mo')
        
        if len(symbols) < 2:
            return jsonify({"error": "At least 2 symbols required"}), 400
        
        if len(symbols) > 5:
            symbols = symbols[:5]
        
        comparison = {}
        
        for symbol in symbols:
            stock_data, error = fetch_stock_data_safe(symbol, period)
            if stock_data:
                # Calculate performance metrics
                prices = [d['Close'] for d in stock_data['data']]
                first_price = prices[0]
                last_price = prices[-1]
                
                comparison[symbol] = {
                    "company_name": stock_data["company_name"],
                    "current_price": stock_data["current_price"],
                    "period_start_price": round(first_price, 2),
                    "period_change_percent": round(((last_price - first_price) / first_price) * 100, 2),
                    "high": round(max(prices), 2),
                    "low": round(min(prices), 2),
                    "volatility": round(np.std(prices), 2)
                }
            time.sleep(REQUEST_DELAY)
        
        return jsonify({
            "period": period,
            "stocks": comparison
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "total_symbols": len(STOCK_SYMBOLS),
        "timestamp": datetime.now().isoformat()
    })


if __name__ == '__main__':
    print(f"Stock ML Backend Starting...")
    print(f"Total stocks in database: {len(STOCK_SYMBOLS)}")
    print(f"Available sectors: {get_all_sectors()}")
    app.run(debug=True, host='0.0.0.0', port=5000)
