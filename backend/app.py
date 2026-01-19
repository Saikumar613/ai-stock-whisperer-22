# ============================================
# COMPLETE STOCK PREDICTION BACKEND
# Flask + MongoDB + JWT Auth + OpenAI
# ============================================
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
from pymongo import MongoClient, ASCENDING, DESCENDING
from bson import ObjectId
import json
import hashlib
import secrets
import jwt
import requests

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["*"], supports_credentials=True)

# Configuration
JWT_SECRET = os.getenv('JWT_SECRET', 'your-super-secret-jwt-key-change-in-production')
JWT_EXPIRY_HOURS = 24
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/stockDB')

# ============================================
# MONGODB CONNECTION & AUTO-SETUP
# ============================================

def setup_database():
    """
    Connect to MongoDB and automatically create collections with indexes.
    Collections are created automatically when first document is inserted.
    """
    try:
        client = MongoClient(MONGODB_URI)
        db = client.get_database()
        
        print(f"✅ Connected to MongoDB: {db.name}")
        
        # Define collections
        collections = {
            'users': db.users,
            'profiles': db.profiles,
            'watchlist': db.watchlist,
            'stock_data': db.stock_data,
            'stock_predictions': db.stock_predictions,
            'chat_messages': db.chat_messages
        }
        
        # Create indexes for better query performance
        collections['users'].create_index('email', unique=True, sparse=True)
        collections['profiles'].create_index('user_id', unique=True)
        collections['watchlist'].create_index([('user_id', ASCENDING), ('symbol', ASCENDING)], unique=True)
        collections['watchlist'].create_index('user_id')
        collections['stock_data'].create_index([('symbol', ASCENDING), ('date', DESCENDING)])
        collections['stock_data'].create_index('symbol')
        collections['stock_predictions'].create_index([('user_id', ASCENDING), ('created_at', DESCENDING)])
        collections['stock_predictions'].create_index('symbol')
        collections['chat_messages'].create_index([('user_id', ASCENDING), ('created_at', ASCENDING)])
        
        print("✅ Database indexes created successfully!")
        print(f"📦 Available collections: {db.list_collection_names()}")
        
        return client, db, collections
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {str(e)}")
        print("💡 Make sure MongoDB is running: mongod --dbpath /path/to/data")
        raise e

# Initialize database connection
client, db, collections = setup_database()

# ============================================
# AUTHENTICATION HELPERS
# ============================================

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token(user_id, email):
    """Generate JWT token"""
    payload = {
        'user_id': str(user_id),
        'email': email,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRY_HOURS),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def verify_token(token):
    """Verify JWT token and return payload"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def get_current_user():
    """Extract user from Authorization header"""
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return None
    
    token = auth_header[7:]  # Remove 'Bearer ' prefix
    payload = verify_token(token)
    if not payload:
        return None
    
    return payload

def require_auth(f):
    """Decorator to require authentication"""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        user = get_current_user()
        if not user:
            return jsonify({'error': 'Authentication required'}), 401
        request.current_user = user
        return f(*args, **kwargs)
    return decorated

def serialize_doc(doc):
    """Convert MongoDB document to JSON-serializable dict"""
    if doc is None:
        return None
    doc['_id'] = str(doc['_id'])
    if 'user_id' in doc and isinstance(doc['user_id'], ObjectId):
        doc['user_id'] = str(doc['user_id'])
    return doc

# ============================================
# AUTH API ENDPOINTS
# ============================================

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """Register a new user"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        password = data.get('password', '')
        full_name = data.get('full_name', '')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400
        
        # Check if user exists
        if collections['users'].find_one({'email': email}):
            return jsonify({'error': 'Email already registered'}), 400
        
        # Create user
        hashed_password = hash_password(password)
        user_result = collections['users'].insert_one({
            'email': email,
            'password': hashed_password,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        })
        
        user_id = str(user_result.inserted_id)
        
        # Create profile
        collections['profiles'].insert_one({
            'user_id': user_id,
            'email': email,
            'full_name': full_name,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        })
        
        # Generate token
        token = generate_token(user_id, email)
        
        print(f"✅ New user registered: {email}")
        
        return jsonify({
            'message': 'Account created successfully',
            'token': token,
            'user': {
                'id': user_id,
                'email': email,
                'full_name': full_name
            }
        }), 201
        
    except Exception as e:
        print(f"❌ Signup error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user and return JWT token"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Find user
        user = collections['users'].find_one({'email': email})
        if not user:
            return jsonify({'error': 'Invalid email or password'}), 401
        
        # Verify password
        if user['password'] != hash_password(password):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        user_id = str(user['_id'])
        
        # Get profile
        profile = collections['profiles'].find_one({'user_id': user_id})
        full_name = profile.get('full_name', '') if profile else ''
        
        # Generate token
        token = generate_token(user_id, email)
        
        print(f"✅ User logged in: {email}")
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user_id,
                'email': email,
                'full_name': full_name,
                'created_at': user.get('created_at', datetime.now()).isoformat()
            }
        }), 200
        
    except Exception as e:
        print(f"❌ Login error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_me():
    """Get current user info"""
    try:
        user = request.current_user
        user_id = user['user_id']
        
        # Get user from DB
        db_user = collections['users'].find_one({'_id': ObjectId(user_id)})
        if not db_user:
            return jsonify({'error': 'User not found'}), 404
        
        # Get profile
        profile = collections['profiles'].find_one({'user_id': user_id})
        
        return jsonify({
            'user': {
                'id': user_id,
                'email': db_user['email'],
                'full_name': profile.get('full_name', '') if profile else '',
                'created_at': db_user.get('created_at', datetime.now()).isoformat()
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/update-password', methods=['POST'])
@require_auth
def update_password():
    """Update user password"""
    try:
        user = request.current_user
        data = request.get_json()
        new_password = data.get('password', '')
        
        if len(new_password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400
        
        collections['users'].update_one(
            {'_id': ObjectId(user['user_id'])},
            {'$set': {
                'password': hash_password(new_password),
                'updated_at': datetime.now()
            }}
        )
        
        return jsonify({'message': 'Password updated successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================
# STOCK SYMBOLS DATABASE
# ============================================

STOCK_SYMBOLS = {
    "Technology": [
        {"symbol": "AAPL", "name": "Apple Inc."},
        {"symbol": "MSFT", "name": "Microsoft Corporation"},
        {"symbol": "GOOGL", "name": "Alphabet Inc."},
        {"symbol": "AMZN", "name": "Amazon.com Inc."},
        {"symbol": "META", "name": "Meta Platforms Inc."},
        {"symbol": "NVDA", "name": "NVIDIA Corporation"},
        {"symbol": "TSLA", "name": "Tesla Inc."},
        {"symbol": "AMD", "name": "Advanced Micro Devices"},
        {"symbol": "INTC", "name": "Intel Corporation"},
        {"symbol": "CRM", "name": "Salesforce Inc."},
        {"symbol": "ORCL", "name": "Oracle Corporation"},
        {"symbol": "ADBE", "name": "Adobe Inc."},
        {"symbol": "CSCO", "name": "Cisco Systems"},
        {"symbol": "IBM", "name": "IBM Corporation"},
        {"symbol": "NFLX", "name": "Netflix Inc."},
    ],
    "Finance": [
        {"symbol": "JPM", "name": "JPMorgan Chase"},
        {"symbol": "BAC", "name": "Bank of America"},
        {"symbol": "WFC", "name": "Wells Fargo"},
        {"symbol": "GS", "name": "Goldman Sachs"},
        {"symbol": "MS", "name": "Morgan Stanley"},
        {"symbol": "V", "name": "Visa Inc."},
        {"symbol": "MA", "name": "Mastercard Inc."},
        {"symbol": "AXP", "name": "American Express"},
        {"symbol": "C", "name": "Citigroup Inc."},
        {"symbol": "BLK", "name": "BlackRock Inc."},
    ],
    "Healthcare": [
        {"symbol": "JNJ", "name": "Johnson & Johnson"},
        {"symbol": "UNH", "name": "UnitedHealth Group"},
        {"symbol": "PFE", "name": "Pfizer Inc."},
        {"symbol": "MRK", "name": "Merck & Co."},
        {"symbol": "ABBV", "name": "AbbVie Inc."},
        {"symbol": "LLY", "name": "Eli Lilly"},
        {"symbol": "TMO", "name": "Thermo Fisher"},
        {"symbol": "ABT", "name": "Abbott Laboratories"},
        {"symbol": "BMY", "name": "Bristol-Myers Squibb"},
        {"symbol": "AMGN", "name": "Amgen Inc."},
    ],
    "Consumer": [
        {"symbol": "WMT", "name": "Walmart Inc."},
        {"symbol": "PG", "name": "Procter & Gamble"},
        {"symbol": "KO", "name": "Coca-Cola Company"},
        {"symbol": "PEP", "name": "PepsiCo Inc."},
        {"symbol": "COST", "name": "Costco Wholesale"},
        {"symbol": "HD", "name": "Home Depot"},
        {"symbol": "MCD", "name": "McDonald's Corp."},
        {"symbol": "NKE", "name": "Nike Inc."},
        {"symbol": "SBUX", "name": "Starbucks Corp."},
        {"symbol": "TGT", "name": "Target Corporation"},
    ],
    "Energy": [
        {"symbol": "XOM", "name": "Exxon Mobil"},
        {"symbol": "CVX", "name": "Chevron Corporation"},
        {"symbol": "COP", "name": "ConocoPhillips"},
        {"symbol": "SLB", "name": "Schlumberger"},
        {"symbol": "EOG", "name": "EOG Resources"},
    ],
    "Indices": [
        {"symbol": "^GSPC", "name": "S&P 500"},
        {"symbol": "^DJI", "name": "Dow Jones"},
        {"symbol": "^IXIC", "name": "NASDAQ"},
        {"symbol": "^RUT", "name": "Russell 2000"},
    ],
    "Indian": [
        {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
        {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
        {"symbol": "INFY.NS", "name": "Infosys Limited"},
        {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
        {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
        {"symbol": "WIPRO.NS", "name": "Wipro Limited"},
        {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
        {"symbol": "ITC.NS", "name": "ITC Limited"},
        {"symbol": "SBIN.NS", "name": "State Bank of India"},
        {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
    ]
}

def get_all_symbols():
    """Get flat list of all symbols"""
    symbols = []
    for sector, stocks in STOCK_SYMBOLS.items():
        for stock in stocks:
            symbols.append({**stock, "sector": sector})
    return symbols

def search_symbols(query):
    """Search symbols by name or symbol"""
    query = query.upper()
    results = []
    for sector, stocks in STOCK_SYMBOLS.items():
        for stock in stocks:
            if query in stock['symbol'].upper() or query in stock['name'].upper():
                results.append({**stock, "sector": sector})
    return results[:20]

# ============================================
# STOCK DATA HELPERS
# ============================================

def fetch_stock_data_safe(symbol, period="1y"):
    """
    Safely fetch stock data from Yahoo Finance.
    yfinance is a Python library that scrapes Yahoo Finance - no API key needed!
    """
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None, "No data found for symbol"
        
        info = stock.info
        
        data = []
        for index, row in hist.iterrows():
            data.append({
                'Date': index.strftime('%Y-%m-%d'),
                'Open': float(row['Open']),
                'High': float(row['High']),
                'Low': float(row['Low']),
                'Close': float(row['Close']),
                'Volume': int(row['Volume'])
            })
        
        return {
            'symbol': symbol,
            'name': info.get('longName', info.get('shortName', symbol)),
            'sector': info.get('sector', 'Unknown'),
            'current_price': float(hist['Close'].iloc[-1]),
            'previous_close': info.get('previousClose', float(hist['Close'].iloc[-2]) if len(hist) > 1 else None),
            'market_cap': info.get('marketCap', None),
            'pe_ratio': info.get('trailingPE', None),
            'data': data
        }, None
        
    except Exception as e:
        return None, str(e)

# ============================================
# STOCK DATA API ENDPOINTS
# ============================================

@app.route('/api/symbols', methods=['GET'])
def get_symbols():
    """Get all available stock symbols"""
    sector = request.args.get('sector')
    search = request.args.get('search')
    
    if search:
        return jsonify(search_symbols(search)), 200
    
    if sector and sector in STOCK_SYMBOLS:
        return jsonify(STOCK_SYMBOLS[sector]), 200
    
    return jsonify(get_all_symbols()), 200

@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Get all available sectors"""
    sectors = []
    for sector, stocks in STOCK_SYMBOLS.items():
        sectors.append({
            'name': sector,
            'count': len(stocks)
        })
    return jsonify(sectors), 200

@app.route('/api/get_stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Fetch stock data from Yahoo Finance and save to MongoDB"""
    try:
        period = request.args.get('period', '1y')
        
        stock_data, error = fetch_stock_data_safe(symbol, period)
        
        if error:
            return jsonify({'error': error}), 404
        
        # Save to MongoDB
        collections['stock_data'].update_one(
            {'symbol': symbol, 'date': datetime.now().strftime('%Y-%m-%d')},
            {
                '$set': {
                    'symbol': symbol,
                    'data': stock_data['data'],
                    'current_price': stock_data['current_price'],
                    'fetched_at': datetime.now()
                }
            },
            upsert=True
        )
        
        print(f"📊 Saved stock data for {symbol} to MongoDB")
        
        return jsonify(stock_data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search/<query>', methods=['GET'])
def search_stocks(query):
    """Search for stocks by name or symbol"""
    results = search_symbols(query)
    
    enriched = []
    for stock in results[:5]:
        try:
            data, _ = fetch_stock_data_safe(stock['symbol'], '5d')
            if data:
                enriched.append({
                    **stock,
                    'current_price': data['current_price'],
                    'name': data['name']
                })
            else:
                enriched.append(stock)
        except:
            enriched.append(stock)
    
    return jsonify(enriched + results[5:]), 200

# ============================================
# PREDICTION API ENDPOINTS
# ============================================

@app.route('/api/predict', methods=['POST'])
@require_auth
def predict():
    """Predict stock price using ML models"""
    try:
        user = request.current_user
        data = request.get_json()
        symbol = data.get('symbol')
        model_type = data.get('model_type', 'RandomForest')
        
        if not symbol:
            return jsonify({'error': 'Symbol is required'}), 400
        
        # Fetch historical data
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if hist.empty:
            return jsonify({'error': 'Stock symbol not found'}), 404
        
        # Prepare data for ML
        df = hist[['Close']].copy()
        df['Prediction'] = df['Close'].shift(-1)
        df = df.dropna()
        
        X = np.array(df[['Close']])
        y = np.array(df['Prediction'])
        
        split = int(0.8 * len(X))
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]
        
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        if model_type == 'SVM':
            model = SVR(kernel='rbf', C=1e3, gamma=0.1)
        elif model_type == 'DecisionTree':
            model = DecisionTreeRegressor(random_state=42)
        else:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        model.fit(X_train_scaled, y_train)
        
        last_price = np.array([[hist['Close'].iloc[-1]]])
        last_price_scaled = scaler.transform(last_price)
        prediction = model.predict(last_price_scaled)[0]
        
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        confidence = max(0, min(1, (train_score + test_score) / 2))
        
        current_price = float(hist['Close'].iloc[-1])
        predicted_price = float(prediction)
        price_change = ((predicted_price - current_price) / current_price) * 100
        
        if price_change > 2:
            recommendation = 'BUY'
        elif price_change < -2:
            recommendation = 'SELL'
        else:
            recommendation = 'HOLD'
        
        result = {
            'symbol': symbol,
            'predicted_price': round(predicted_price, 2),
            'current_price': round(current_price, 2),
            'price_change_percent': round(price_change, 2),
            'confidence': round(confidence * 100, 1),
            'model_type': model_type,
            'recommendation': recommendation,
            'prediction_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save prediction to MongoDB
        collections['stock_predictions'].insert_one({
            'user_id': user['user_id'],
            'symbol': symbol,
            'predicted_price': predicted_price,
            'current_price': current_price,
            'confidence': confidence,
            'model_type': model_type,
            'recommendation': recommendation,
            'created_at': datetime.now()
        })
        
        print(f"🔮 Saved prediction for {symbol} to MongoDB")
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predictions', methods=['GET'])
@require_auth
def get_user_predictions():
    """Get prediction history for current user"""
    try:
        user = request.current_user
        predictions = list(
            collections['stock_predictions']
            .find({'user_id': user['user_id']})
            .sort('created_at', DESCENDING)
            .limit(50)
        )
        
        return jsonify([serialize_doc(p) for p in predictions]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================
# WATCHLIST API ENDPOINTS
# ============================================

@app.route('/api/watchlist', methods=['GET'])
@require_auth
def get_watchlist():
    """Get user's watchlist"""
    try:
        user = request.current_user
        watchlist = list(collections['watchlist'].find({'user_id': user['user_id']}))
        
        # Enrich with current prices
        enriched = []
        for item in watchlist:
            try:
                stock_data, _ = fetch_stock_data_safe(item['symbol'], '5d')
                enriched.append({
                    **serialize_doc(item),
                    'current_price': stock_data['current_price'] if stock_data else None
                })
            except:
                enriched.append(serialize_doc(item))
        
        return jsonify(enriched), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/watchlist', methods=['POST'])
@require_auth
def add_to_watchlist():
    """Add stock to watchlist"""
    try:
        user = request.current_user
        data = request.get_json()
        symbol = data.get('symbol', '').upper()
        company_name = data.get('company_name', symbol)
        
        if not symbol:
            return jsonify({'error': 'Symbol is required'}), 400
        
        # Check if already exists
        existing = collections['watchlist'].find_one({
            'user_id': user['user_id'],
            'symbol': symbol
        })
        
        if existing:
            return jsonify({'error': 'Already in watchlist', 'code': 'DUPLICATE'}), 400
        
        result = collections['watchlist'].insert_one({
            'user_id': user['user_id'],
            'symbol': symbol,
            'company_name': company_name,
            'added_at': datetime.now()
        })
        
        print(f"📌 Added {symbol} to watchlist for user {user['user_id']}")
        
        return jsonify({
            'message': 'Added to watchlist',
            'id': str(result.inserted_id),
            'symbol': symbol
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/watchlist/<item_id>', methods=['DELETE'])
@require_auth
def remove_from_watchlist(item_id):
    """Remove stock from watchlist"""
    try:
        user = request.current_user
        result = collections['watchlist'].delete_one({
            '_id': ObjectId(item_id),
            'user_id': user['user_id']
        })
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Not found in watchlist'}), 404
        
        return jsonify({'message': 'Removed from watchlist'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================
# CHAT API ENDPOINTS (with OpenAI)
# ============================================

@app.route('/api/chat/history', methods=['GET'])
@require_auth
def get_chat_history():
    """Get chat history for current user"""
    try:
        user = request.current_user
        messages = list(
            collections['chat_messages']
            .find({'user_id': user['user_id']})
            .sort('created_at', ASCENDING)
            .limit(100)
        )
        
        return jsonify([serialize_doc(m) for m in messages]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
@require_auth
def chat():
    """Send message and get AI response using OpenAI"""
    try:
        user = request.current_user
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Save user message
        collections['chat_messages'].insert_one({
            'user_id': user['user_id'],
            'content': message,
            'role': 'user',
            'created_at': datetime.now()
        })
        
        # Generate AI response
        if OPENAI_API_KEY:
            # Use OpenAI API
            try:
                response = requests.post(
                    'https://api.openai.com/v1/chat/completions',
                    headers={
                        'Authorization': f'Bearer {OPENAI_API_KEY}',
                        'Content-Type': 'application/json'
                    },
                    json={
                        'model': 'gpt-3.5-turbo',
                        'messages': [
                            {
                                'role': 'system',
                                'content': '''You are an AI Investment Assistant specialized in stock market analysis. 
                                You help users understand stocks, market trends, and investment strategies.
                                Provide clear, actionable insights while noting that this is for educational purposes only.
                                Always remind users to do their own research and consult financial advisors for major decisions.'''
                            },
                            {'role': 'user', 'content': message}
                        ],
                        'max_tokens': 500,
                        'temperature': 0.7
                    },
                    timeout=30
                )
                
                if response.status_code == 200:
                    ai_response = response.json()['choices'][0]['message']['content']
                else:
                    ai_response = f"I apologize, but I'm having trouble connecting to the AI service. Error: {response.status_code}"
                    
            except Exception as e:
                ai_response = f"I'm having trouble processing your request. Please try again. Error: {str(e)}"
        else:
            # Fallback response when no API key
            ai_response = generate_fallback_response(message)
        
        # Save AI response
        collections['chat_messages'].insert_one({
            'user_id': user['user_id'],
            'content': ai_response,
            'role': 'assistant',
            'created_at': datetime.now()
        })
        
        return jsonify({
            'response': ai_response,
            'message': 'Success'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_fallback_response(message):
    """Generate a helpful response without OpenAI"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm your AI Investment Assistant. I can help you analyze stocks, understand market trends, and learn about investment strategies. What would you like to know?"
    
    if any(word in message_lower for word in ['buy', 'sell', 'invest']):
        return """When considering whether to buy or sell a stock, consider these factors:

1. **Fundamental Analysis**: Look at the company's earnings, revenue growth, and financial health
2. **Technical Analysis**: Study price charts, moving averages, and trading volume
3. **Market Conditions**: Consider the broader market trends and economic indicators
4. **Risk Tolerance**: Ensure the investment aligns with your risk profile

Always do thorough research and consider consulting a financial advisor for personalized advice."""

    if any(word in message_lower for word in ['predict', 'forecast', 'future']):
        return """Stock price predictions can be made using various methods:

1. **Machine Learning Models**: SVM, Random Forest, and LSTM neural networks
2. **Technical Indicators**: Moving averages, RSI, MACD
3. **Fundamental Analysis**: Earnings forecasts, industry trends

Use our Prediction feature on the Dashboard to get ML-powered price predictions for any stock!

Remember: No prediction is 100% accurate. Always invest responsibly."""

    if any(word in message_lower for word in ['risk', 'safe', 'protect']):
        return """Here are key risk management strategies:

1. **Diversification**: Don't put all eggs in one basket
2. **Stop-Loss Orders**: Set automatic sell points to limit losses
3. **Position Sizing**: Never risk more than 1-2% of your portfolio on a single trade
4. **Regular Rebalancing**: Maintain your target asset allocation

Would you like to learn more about any of these strategies?"""

    return """I'm here to help with your investment questions! You can ask me about:

• Stock analysis and predictions
• Market trends and indicators
• Investment strategies
• Risk management
• How to use this platform's features

What would you like to know?"""

# ============================================
# HEALTH CHECK & DATABASE INFO
# ============================================

@app.route('/health', methods=['GET'])
def health_check():
    """Check API and database health"""
    try:
        client.admin.command('ping')
        
        collection_stats = {}
        for name in db.list_collection_names():
            collection_stats[name] = db[name].count_documents({})
        
        return jsonify({
            'status': 'healthy',
            'database': db.name,
            'collections': collection_stats,
            'openai_configured': bool(OPENAI_API_KEY),
            'message': 'Flask API + MongoDB is running!'
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

@app.route('/api/db-info', methods=['GET'])
def database_info():
    """Get detailed database information"""
    try:
        info = {
            'database_name': db.name,
            'collections': [],
            'connection_string': MONGODB_URI.split('@')[-1] if '@' in MONGODB_URI else MONGODB_URI
        }
        
        for name in db.list_collection_names():
            coll = db[name]
            info['collections'].append({
                'name': name,
                'document_count': coll.count_documents({}),
                'indexes': list(coll.index_information().keys())
            })
        
        return jsonify(info), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================
# RUN THE APP
# ============================================

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 STOCK PREDICTION API")
    print("="*50)
    print(f"📊 Database: {db.name}")
    print(f"🔗 API URL: http://localhost:5000")
    print(f"❤️  Health: http://localhost:5000/health")
    print(f"🤖 OpenAI: {'Configured' if OPENAI_API_KEY else 'Not configured (using fallback)'}")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
