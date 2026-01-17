# 🚀 STOCK PREDICTION APP - FRESH REPOSITORY

## Complete MongoDB-Based Solution (No Supabase)

**MongoDB Connection:** `mongodb://localhost:27017/stockDB`

---

# 📁 FOLDER STRUCTURE

```
stock-prediction-app/
│
├── frontend/                    # React + TypeScript + Vite
│   ├── public/
│   │   ├── favicon.ico
│   │   └── robots.txt
│   ├── src/
│   │   ├── assets/
│   │   │   └── logo.png
│   │   ├── components/
│   │   │   ├── ui/              # shadcn components
│   │   │   ├── Navbar.tsx
│   │   │   ├── StockSearch.tsx
│   │   │   ├── StockChart.tsx
│   │   │   ├── Watchlist.tsx
│   │   │   ├── PredictionCard.tsx
│   │   │   └── TrendChart.tsx
│   │   ├── contexts/
│   │   │   └── AuthContext.tsx
│   │   ├── hooks/
│   │   │   └── use-toast.ts
│   │   ├── lib/
│   │   │   └── utils.ts
│   │   ├── pages/
│   │   │   ├── Index.tsx
│   │   │   ├── Auth.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Profile.tsx
│   │   │   ├── Chat.tsx
│   │   │   └── NotFound.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   └── stockApi.ts
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.tsx
│   ├── .env
│   ├── index.html
│   ├── package.json
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── backend/                     # Flask + Python
│   ├── app.py                   # Main Flask application
│   ├── config.py                # Configuration management
│   ├── stock_symbols.py         # Stock symbols database
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

# 🔧 BACKEND FILES

## 1. backend/.env

```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/stockDB

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000

# JWT Configuration
JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production-2024

# CORS Configuration
CORS_ORIGINS=http://localhost:8080,http://localhost:3000,http://localhost:5173
```

---

## 2. backend/config.py

```python
# ============================================
# CONFIGURATION MANAGEMENT
# ============================================

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/stockDB')
    
    # Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))
    
    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5173').split(',')

config = Config()
```

---

## 3. backend/stock_symbols.py

```python
# ============================================
# COMPREHENSIVE STOCK SYMBOLS DATABASE
# ============================================

STOCK_SYMBOLS = {
    "Technology": [
        {"symbol": "AAPL", "name": "Apple Inc."},
        {"symbol": "MSFT", "name": "Microsoft Corporation"},
        {"symbol": "GOOGL", "name": "Alphabet Inc. Class A"},
        {"symbol": "GOOG", "name": "Alphabet Inc. Class C"},
        {"symbol": "AMZN", "name": "Amazon.com Inc."},
        {"symbol": "META", "name": "Meta Platforms Inc."},
        {"symbol": "NVDA", "name": "NVIDIA Corporation"},
        {"symbol": "TSLA", "name": "Tesla Inc."},
        {"symbol": "AMD", "name": "Advanced Micro Devices"},
        {"symbol": "INTC", "name": "Intel Corporation"},
        {"symbol": "CRM", "name": "Salesforce Inc."},
        {"symbol": "ORCL", "name": "Oracle Corporation"},
        {"symbol": "ADBE", "name": "Adobe Inc."},
        {"symbol": "CSCO", "name": "Cisco Systems Inc."},
        {"symbol": "IBM", "name": "IBM Corporation"},
        {"symbol": "QCOM", "name": "Qualcomm Inc."},
        {"symbol": "TXN", "name": "Texas Instruments"},
        {"symbol": "AVGO", "name": "Broadcom Inc."},
        {"symbol": "NOW", "name": "ServiceNow Inc."},
        {"symbol": "SNOW", "name": "Snowflake Inc."},
        {"symbol": "PLTR", "name": "Palantir Technologies"},
        {"symbol": "NET", "name": "Cloudflare Inc."},
        {"symbol": "CRWD", "name": "CrowdStrike Holdings"},
        {"symbol": "ZS", "name": "Zscaler Inc."},
        {"symbol": "DDOG", "name": "Datadog Inc."},
        {"symbol": "MDB", "name": "MongoDB Inc."},
        {"symbol": "SHOP", "name": "Shopify Inc."},
        {"symbol": "SQ", "name": "Block Inc."},
        {"symbol": "PYPL", "name": "PayPal Holdings"},
        {"symbol": "UBER", "name": "Uber Technologies"},
        {"symbol": "LYFT", "name": "Lyft Inc."},
        {"symbol": "ABNB", "name": "Airbnb Inc."},
        {"symbol": "DOCU", "name": "DocuSign Inc."},
        {"symbol": "ZM", "name": "Zoom Video Communications"},
        {"symbol": "TWLO", "name": "Twilio Inc."},
    ],
    "Finance": [
        {"symbol": "JPM", "name": "JPMorgan Chase & Co."},
        {"symbol": "BAC", "name": "Bank of America Corp."},
        {"symbol": "WFC", "name": "Wells Fargo & Co."},
        {"symbol": "GS", "name": "Goldman Sachs Group"},
        {"symbol": "MS", "name": "Morgan Stanley"},
        {"symbol": "C", "name": "Citigroup Inc."},
        {"symbol": "BLK", "name": "BlackRock Inc."},
        {"symbol": "SCHW", "name": "Charles Schwab Corp."},
        {"symbol": "AXP", "name": "American Express Co."},
        {"symbol": "V", "name": "Visa Inc."},
        {"symbol": "MA", "name": "Mastercard Inc."},
        {"symbol": "COF", "name": "Capital One Financial"},
        {"symbol": "USB", "name": "U.S. Bancorp"},
        {"symbol": "PNC", "name": "PNC Financial Services"},
        {"symbol": "TFC", "name": "Truist Financial Corp."},
        {"symbol": "SPGI", "name": "S&P Global Inc."},
        {"symbol": "ICE", "name": "Intercontinental Exchange"},
        {"symbol": "CME", "name": "CME Group Inc."},
        {"symbol": "MCO", "name": "Moody's Corporation"},
        {"symbol": "COIN", "name": "Coinbase Global Inc."},
    ],
    "Healthcare": [
        {"symbol": "JNJ", "name": "Johnson & Johnson"},
        {"symbol": "UNH", "name": "UnitedHealth Group"},
        {"symbol": "PFE", "name": "Pfizer Inc."},
        {"symbol": "ABBV", "name": "AbbVie Inc."},
        {"symbol": "MRK", "name": "Merck & Co."},
        {"symbol": "LLY", "name": "Eli Lilly and Co."},
        {"symbol": "TMO", "name": "Thermo Fisher Scientific"},
        {"symbol": "ABT", "name": "Abbott Laboratories"},
        {"symbol": "DHR", "name": "Danaher Corporation"},
        {"symbol": "BMY", "name": "Bristol-Myers Squibb"},
        {"symbol": "AMGN", "name": "Amgen Inc."},
        {"symbol": "GILD", "name": "Gilead Sciences"},
        {"symbol": "MRNA", "name": "Moderna Inc."},
        {"symbol": "REGN", "name": "Regeneron Pharmaceuticals"},
        {"symbol": "VRTX", "name": "Vertex Pharmaceuticals"},
        {"symbol": "ISRG", "name": "Intuitive Surgical"},
        {"symbol": "SYK", "name": "Stryker Corporation"},
        {"symbol": "MDT", "name": "Medtronic PLC"},
        {"symbol": "ZTS", "name": "Zoetis Inc."},
        {"symbol": "CVS", "name": "CVS Health Corp."},
    ],
    "Consumer": [
        {"symbol": "WMT", "name": "Walmart Inc."},
        {"symbol": "PG", "name": "Procter & Gamble"},
        {"symbol": "KO", "name": "Coca-Cola Company"},
        {"symbol": "PEP", "name": "PepsiCo Inc."},
        {"symbol": "COST", "name": "Costco Wholesale"},
        {"symbol": "HD", "name": "Home Depot Inc."},
        {"symbol": "MCD", "name": "McDonald's Corp."},
        {"symbol": "NKE", "name": "Nike Inc."},
        {"symbol": "SBUX", "name": "Starbucks Corp."},
        {"symbol": "TGT", "name": "Target Corporation"},
        {"symbol": "LOW", "name": "Lowe's Companies"},
        {"symbol": "DIS", "name": "Walt Disney Co."},
        {"symbol": "NFLX", "name": "Netflix Inc."},
        {"symbol": "CMCSA", "name": "Comcast Corporation"},
        {"symbol": "VZ", "name": "Verizon Communications"},
        {"symbol": "T", "name": "AT&T Inc."},
        {"symbol": "TMUS", "name": "T-Mobile US Inc."},
        {"symbol": "CL", "name": "Colgate-Palmolive"},
        {"symbol": "EL", "name": "Estée Lauder Companies"},
        {"symbol": "LULU", "name": "Lululemon Athletica"},
    ],
    "Energy": [
        {"symbol": "XOM", "name": "Exxon Mobil Corp."},
        {"symbol": "CVX", "name": "Chevron Corporation"},
        {"symbol": "COP", "name": "ConocoPhillips"},
        {"symbol": "SLB", "name": "Schlumberger Limited"},
        {"symbol": "EOG", "name": "EOG Resources"},
        {"symbol": "MPC", "name": "Marathon Petroleum"},
        {"symbol": "PSX", "name": "Phillips 66"},
        {"symbol": "VLO", "name": "Valero Energy"},
        {"symbol": "OXY", "name": "Occidental Petroleum"},
        {"symbol": "HAL", "name": "Halliburton Company"},
        {"symbol": "DVN", "name": "Devon Energy Corp."},
        {"symbol": "KMI", "name": "Kinder Morgan Inc."},
        {"symbol": "WMB", "name": "Williams Companies"},
        {"symbol": "OKE", "name": "ONEOK Inc."},
        {"symbol": "ENPH", "name": "Enphase Energy"},
    ],
    "Industrial": [
        {"symbol": "CAT", "name": "Caterpillar Inc."},
        {"symbol": "BA", "name": "Boeing Company"},
        {"symbol": "HON", "name": "Honeywell International"},
        {"symbol": "UPS", "name": "United Parcel Service"},
        {"symbol": "RTX", "name": "RTX Corporation"},
        {"symbol": "LMT", "name": "Lockheed Martin"},
        {"symbol": "GE", "name": "General Electric"},
        {"symbol": "MMM", "name": "3M Company"},
        {"symbol": "DE", "name": "Deere & Company"},
        {"symbol": "UNP", "name": "Union Pacific Corp."},
        {"symbol": "FDX", "name": "FedEx Corporation"},
        {"symbol": "CSX", "name": "CSX Corporation"},
        {"symbol": "NSC", "name": "Norfolk Southern"},
        {"symbol": "GD", "name": "General Dynamics"},
        {"symbol": "NOC", "name": "Northrop Grumman"},
    ],
    "ETFs": [
        {"symbol": "SPY", "name": "SPDR S&P 500 ETF"},
        {"symbol": "QQQ", "name": "Invesco QQQ Trust"},
        {"symbol": "IWM", "name": "iShares Russell 2000 ETF"},
        {"symbol": "DIA", "name": "SPDR Dow Jones ETF"},
        {"symbol": "VTI", "name": "Vanguard Total Stock Market"},
        {"symbol": "VOO", "name": "Vanguard S&P 500 ETF"},
        {"symbol": "VGT", "name": "Vanguard Information Technology"},
        {"symbol": "XLF", "name": "Financial Select Sector SPDR"},
        {"symbol": "XLK", "name": "Technology Select Sector SPDR"},
        {"symbol": "XLE", "name": "Energy Select Sector SPDR"},
        {"symbol": "XLV", "name": "Health Care Select Sector SPDR"},
        {"symbol": "ARKK", "name": "ARK Innovation ETF"},
        {"symbol": "ARKG", "name": "ARK Genomic Revolution ETF"},
        {"symbol": "GLD", "name": "SPDR Gold Shares"},
        {"symbol": "SLV", "name": "iShares Silver Trust"},
    ],
    "International": [
        {"symbol": "BABA", "name": "Alibaba Group"},
        {"symbol": "TSM", "name": "Taiwan Semiconductor"},
        {"symbol": "NVO", "name": "Novo Nordisk"},
        {"symbol": "ASML", "name": "ASML Holding"},
        {"symbol": "TM", "name": "Toyota Motor Corp."},
        {"symbol": "SONY", "name": "Sony Group Corp."},
        {"symbol": "SAP", "name": "SAP SE"},
        {"symbol": "NVS", "name": "Novartis AG"},
        {"symbol": "AZN", "name": "AstraZeneca PLC"},
        {"symbol": "HSBC", "name": "HSBC Holdings"},
        {"symbol": "BP", "name": "BP PLC"},
        {"symbol": "SHEL", "name": "Shell PLC"},
        {"symbol": "RIO", "name": "Rio Tinto Group"},
        {"symbol": "BHP", "name": "BHP Group Limited"},
        {"symbol": "UL", "name": "Unilever PLC"},
    ],
    "Crypto_Related": [
        {"symbol": "COIN", "name": "Coinbase Global"},
        {"symbol": "MSTR", "name": "MicroStrategy Inc."},
        {"symbol": "SQ", "name": "Block Inc."},
        {"symbol": "PYPL", "name": "PayPal Holdings"},
        {"symbol": "RIOT", "name": "Riot Platforms"},
        {"symbol": "MARA", "name": "Marathon Digital"},
        {"symbol": "HOOD", "name": "Robinhood Markets"},
    ],
    "Real_Estate": [
        {"symbol": "AMT", "name": "American Tower Corp."},
        {"symbol": "PLD", "name": "Prologis Inc."},
        {"symbol": "CCI", "name": "Crown Castle Inc."},
        {"symbol": "EQIX", "name": "Equinix Inc."},
        {"symbol": "SPG", "name": "Simon Property Group"},
        {"symbol": "O", "name": "Realty Income Corp."},
        {"symbol": "WELL", "name": "Welltower Inc."},
        {"symbol": "DLR", "name": "Digital Realty Trust"},
        {"symbol": "AVB", "name": "AvalonBay Communities"},
        {"symbol": "EQR", "name": "Equity Residential"},
    ]
}


def get_all_symbols():
    """Get flat list of all stock symbols"""
    symbols = []
    for sector, stocks in STOCK_SYMBOLS.items():
        for stock in stocks:
            stock_with_sector = stock.copy()
            stock_with_sector['sector'] = sector
            symbols.append(stock_with_sector)
    return symbols


def get_symbols_by_sector(sector):
    """Get stocks by sector"""
    return STOCK_SYMBOLS.get(sector, [])


def get_stock_info(symbol):
    """Get stock info by symbol"""
    symbol = symbol.upper()
    for sector, stocks in STOCK_SYMBOLS.items():
        for stock in stocks:
            if stock['symbol'] == symbol:
                return {**stock, 'sector': sector}
    return None


def get_all_sectors():
    """Get list of all sectors"""
    return list(STOCK_SYMBOLS.keys())


def search_stocks(query):
    """Search stocks by name or symbol"""
    query = query.lower()
    results = []
    for sector, stocks in STOCK_SYMBOLS.items():
        for stock in stocks:
            if query in stock['symbol'].lower() or query in stock['name'].lower():
                results.append({**stock, 'sector': sector})
    return results
```

---

## 4. backend/requirements.txt

```txt
flask==3.0.0
flask-cors==4.0.0
flask-jwt-extended==4.6.0
pymongo==4.6.1
python-dotenv==1.0.0
yfinance==0.2.36
numpy==1.26.3
pandas==2.1.4
scikit-learn==1.3.2
bcrypt==4.1.2
gunicorn==21.2.0
requests==2.31.0
```

---

## 5. backend/app.py

```python
# ============================================
# STOCK PREDICTION BACKEND - MONGODB BASED
# ============================================
# MongoDB: mongodb://localhost:27017/stockDB
# Run: python app.py
# Port: 5000
# ============================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import bcrypt
from pymongo import MongoClient
from bson import ObjectId
import time

from config import config
from stock_symbols import (
    get_all_symbols, get_symbols_by_sector, get_stock_info,
    get_all_sectors, search_stocks, STOCK_SYMBOLS
)

# Initialize Flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=config.JWT_ACCESS_TOKEN_EXPIRES)

# Enable CORS
CORS(app, origins=config.CORS_ORIGINS, supports_credentials=True)

# Initialize JWT
jwt = JWTManager(app)

# ============================================
# MONGODB CONNECTION
# ============================================

try:
    client = MongoClient(config.MONGODB_URI)
    db = client.stockDB
    
    # Collections
    users_collection = db.users
    profiles_collection = db.profiles
    watchlist_collection = db.watchlist
    stock_data_collection = db.stock_data
    predictions_collection = db.stock_predictions
    chat_messages_collection = db.chat_messages
    
    # Create indexes
    users_collection.create_index('email', unique=True)
    watchlist_collection.create_index([('user_id', 1), ('symbol', 1)], unique=True)
    
    print("✅ Connected to MongoDB: stockDB")
except Exception as e:
    print(f"❌ MongoDB connection failed: {str(e)}")

# ============================================
# HELPER FUNCTIONS
# ============================================

def serialize_doc(doc):
    """Convert MongoDB document to JSON serializable"""
    if doc is None:
        return None
    doc['id'] = str(doc.pop('_id'))
    return doc


def fetch_stock_data_safe(symbol, period="1y"):
    """Safely fetch stock data with error handling"""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None
        
        info = stock.info
        current_price = hist['Close'].iloc[-1]
        prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
        change = current_price - prev_close
        change_percent = (change / prev_close) * 100 if prev_close > 0 else 0
        
        return {
            'symbol': symbol,
            'name': info.get('shortName', info.get('longName', symbol)),
            'current_price': float(current_price),
            'previous_close': float(prev_close),
            'change': float(change),
            'change_percent': float(change_percent),
            'high': float(hist['High'].iloc[-1]),
            'low': float(hist['Low'].iloc[-1]),
            'open': float(hist['Open'].iloc[-1]),
            'volume': int(hist['Volume'].iloc[-1]),
            'market_cap': info.get('marketCap'),
            'pe_ratio': info.get('trailingPE'),
            'dividend_yield': info.get('dividendYield'),
            'fifty_two_week_high': info.get('fiftyTwoWeekHigh'),
            'fifty_two_week_low': info.get('fiftyTwoWeekLow'),
            'history': hist.reset_index().to_dict('records'),
            'fetched_at': datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Error fetching {symbol}: {str(e)}")
        return None


# ============================================
# AUTHENTICATION ENDPOINTS
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
        if users_collection.find_one({'email': email}):
            return jsonify({'error': 'Email already registered'}), 409
        
        # Hash password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create user
        user_doc = {
            'email': email,
            'password_hash': password_hash,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        result = users_collection.insert_one(user_doc)
        user_id = str(result.inserted_id)
        
        # Create profile
        profile_doc = {
            'user_id': user_id,
            'email': email,
            'full_name': full_name,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        profiles_collection.insert_one(profile_doc)
        
        # Generate token
        access_token = create_access_token(identity=user_id)
        
        return jsonify({
            'message': 'User registered successfully',
            'user': {
                'id': user_id,
                'email': email,
                'full_name': full_name
            },
            'access_token': access_token
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        # Find user
        user = users_collection.find_one({'email': email})
        if not user:
            return jsonify({'error': 'Invalid email or password'}), 401
        
        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user['password_hash']):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        user_id = str(user['_id'])
        
        # Get profile
        profile = profiles_collection.find_one({'user_id': user_id})
        
        # Generate token
        access_token = create_access_token(identity=user_id)
        
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user_id,
                'email': email,
                'full_name': profile.get('full_name', '') if profile else ''
            },
            'access_token': access_token
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current authenticated user"""
    try:
        user_id = get_jwt_identity()
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        profile = profiles_collection.find_one({'user_id': user_id})
        
        return jsonify({
            'user': {
                'id': user_id,
                'email': user['email'],
                'full_name': profile.get('full_name', '') if profile else ''
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    """Logout user (client should discard token)"""
    return jsonify({'message': 'Logged out successfully'}), 200


# ============================================
# PROFILE ENDPOINTS
# ============================================

@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get user profile"""
    try:
        user_id = get_jwt_identity()
        profile = profiles_collection.find_one({'user_id': user_id})
        
        if not profile:
            return jsonify({'error': 'Profile not found'}), 404
        
        return jsonify(serialize_doc(profile)), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update user profile"""
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        update_data = {
            'updated_at': datetime.now()
        }
        
        if 'full_name' in data:
            update_data['full_name'] = data['full_name']
        if 'email' in data:
            update_data['email'] = data['email']
        
        result = profiles_collection.update_one(
            {'user_id': user_id},
            {'$set': update_data}
        )
        
        if result.matched_count == 0:
            return jsonify({'error': 'Profile not found'}), 404
        
        profile = profiles_collection.find_one({'user_id': user_id})
        return jsonify(serialize_doc(profile)), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# STOCK SYMBOLS ENDPOINTS
# ============================================

@app.route('/api/symbols', methods=['GET'])
def get_symbols():
    """Get all stock symbols with optional filtering"""
    sector = request.args.get('sector')
    query = request.args.get('search')
    
    if query:
        return jsonify(search_stocks(query)), 200
    elif sector:
        stocks = get_symbols_by_sector(sector)
        return jsonify([{**s, 'sector': sector} for s in stocks]), 200
    else:
        return jsonify(get_all_symbols()), 200


@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Get all sectors with stock counts"""
    sectors = []
    for sector, stocks in STOCK_SYMBOLS.items():
        sectors.append({
            'name': sector,
            'count': len(stocks)
        })
    return jsonify(sectors), 200


@app.route('/api/search/<query>', methods=['GET'])
def search_stocks_endpoint(query):
    """Search for stocks"""
    results = search_stocks(query)
    
    # Add live data for top 5 results
    enriched = []
    for stock in results[:5]:
        live_data = fetch_stock_data_safe(stock['symbol'], period='5d')
        if live_data:
            enriched.append({**stock, **live_data})
        else:
            enriched.append(stock)
        time.sleep(0.2)  # Rate limiting
    
    # Add remaining without live data
    enriched.extend(results[5:])
    
    return jsonify(enriched), 200


# ============================================
# STOCK DATA ENDPOINTS
# ============================================

@app.route('/api/get_stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Get detailed stock data"""
    try:
        period = request.args.get('period', '1y')
        data = fetch_stock_data_safe(symbol.upper(), period)
        
        if not data:
            return jsonify({'error': 'Stock symbol not found'}), 404
        
        # Save to MongoDB
        stock_data_collection.update_one(
            {'symbol': symbol.upper()},
            {'$set': data},
            upsert=True
        )
        
        return jsonify(data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/get_multiple_stocks', methods=['POST'])
def get_multiple_stocks():
    """Fetch data for multiple stocks"""
    try:
        data = request.get_json()
        symbols = data.get('symbols', [])[:50]  # Limit to 50
        
        results = []
        errors = []
        
        for symbol in symbols:
            stock_data = fetch_stock_data_safe(symbol, period='5d')
            if stock_data:
                results.append(stock_data)
            else:
                errors.append(symbol)
            time.sleep(0.2)  # Rate limiting
        
        return jsonify({
            'data': results,
            'errors': errors,
            'total_requested': len(symbols),
            'total_success': len(results)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/market_overview', methods=['GET'])
def market_overview():
    """Get market overview with major indices"""
    try:
        indices = ['SPY', 'QQQ', 'DIA', 'IWM', 'VTI']
        top_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA']
        
        index_data = []
        for symbol in indices:
            data = fetch_stock_data_safe(symbol, period='5d')
            if data:
                index_data.append(data)
            time.sleep(0.2)
        
        stock_data = []
        for symbol in top_stocks:
            data = fetch_stock_data_safe(symbol, period='5d')
            if data:
                stock_data.append(data)
            time.sleep(0.2)
        
        return jsonify({
            'indices': index_data,
            'top_stocks': stock_data,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/get_sector_stocks/<sector>', methods=['GET'])
def get_sector_stocks(sector):
    """Get stocks for a specific sector with live data"""
    try:
        stocks = get_symbols_by_sector(sector)
        if not stocks:
            return jsonify({'error': 'Sector not found'}), 404
        
        limit = min(int(request.args.get('limit', 10)), 20)
        results = []
        
        for stock in stocks[:limit]:
            data = fetch_stock_data_safe(stock['symbol'], period='5d')
            if data:
                results.append({**stock, **data, 'sector': sector})
            time.sleep(0.2)
        
        return jsonify({
            'sector': sector,
            'stocks': results,
            'total_in_sector': len(stocks)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# WATCHLIST ENDPOINTS
# ============================================

@app.route('/api/watchlist', methods=['GET'])
@jwt_required()
def get_watchlist():
    """Get user's watchlist"""
    try:
        user_id = get_jwt_identity()
        watchlist = list(watchlist_collection.find({'user_id': user_id}))
        
        # Enrich with live data
        enriched = []
        for item in watchlist:
            data = fetch_stock_data_safe(item['symbol'], period='5d')
            enriched_item = serialize_doc(item)
            if data:
                enriched_item.update({
                    'current_price': data['current_price'],
                    'change': data['change'],
                    'change_percent': data['change_percent']
                })
            enriched.append(enriched_item)
            time.sleep(0.1)
        
        return jsonify(enriched), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/watchlist', methods=['POST'])
@jwt_required()
def add_to_watchlist():
    """Add stock to watchlist"""
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        symbol = data.get('symbol', '').upper()
        
        if not symbol:
            return jsonify({'error': 'Symbol is required'}), 400
        
        # Get stock info
        stock_info = get_stock_info(symbol)
        company_name = stock_info['name'] if stock_info else symbol
        
        # Check if already in watchlist
        existing = watchlist_collection.find_one({
            'user_id': user_id,
            'symbol': symbol
        })
        
        if existing:
            return jsonify({'error': 'Stock already in watchlist'}), 409
        
        # Add to watchlist
        doc = {
            'user_id': user_id,
            'symbol': symbol,
            'company_name': company_name,
            'added_at': datetime.now()
        }
        result = watchlist_collection.insert_one(doc)
        doc['id'] = str(result.inserted_id)
        del doc['_id']
        
        return jsonify(doc), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/watchlist/<symbol>', methods=['DELETE'])
@jwt_required()
def remove_from_watchlist(symbol):
    """Remove stock from watchlist"""
    try:
        user_id = get_jwt_identity()
        result = watchlist_collection.delete_one({
            'user_id': user_id,
            'symbol': symbol.upper()
        })
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Stock not found in watchlist'}), 404
        
        return jsonify({'message': 'Removed from watchlist'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# PREDICTION ENDPOINTS
# ============================================

@app.route('/api/predict', methods=['POST'])
@jwt_required(optional=True)
def predict():
    """Predict stock price using ML models"""
    try:
        data = request.get_json()
        symbol = data.get('symbol', '').upper()
        model_type = data.get('model_type', 'RandomForest')
        
        user_id = get_jwt_identity()
        
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
        
        X = np.array(df[['Close']])
        y = np.array(df['Prediction'])
        
        # Split data
        split = int(0.8 * len(X))
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]
        
        # Scale data
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Select model
        if model_type == 'SVM':
            model = SVR(kernel='rbf', C=1e3, gamma=0.1)
        elif model_type == 'DecisionTree':
            model = DecisionTreeRegressor(random_state=42)
        else:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model_type = 'RandomForest'
        
        # Train
        model.fit(X_train_scaled, y_train)
        
        # Predict
        last_price = np.array([[hist['Close'].iloc[-1]]])
        last_price_scaled = scaler.transform(last_price)
        prediction = model.predict(last_price_scaled)[0]
        
        # Confidence
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        confidence = (train_score + test_score) / 2
        
        result = {
            'symbol': symbol,
            'predicted_price': float(prediction),
            'current_price': float(hist['Close'].iloc[-1]),
            'confidence': float(confidence),
            'model_type': model_type,
            'prediction_date': datetime.now().isoformat()
        }
        
        # Save prediction
        if user_id:
            predictions_collection.insert_one({
                **result,
                'user_id': user_id,
                'created_at': datetime.now()
            })
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/predictions/history', methods=['GET'])
@jwt_required()
def get_prediction_history():
    """Get user's prediction history"""
    try:
        user_id = get_jwt_identity()
        limit = int(request.args.get('limit', 20))
        
        predictions = list(
            predictions_collection.find({'user_id': user_id})
            .sort('created_at', -1)
            .limit(limit)
        )
        
        return jsonify([serialize_doc(p) for p in predictions]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# CHAT ENDPOINTS
# ============================================

@app.route('/api/chat/messages', methods=['GET'])
@jwt_required()
def get_chat_messages():
    """Get user's chat history"""
    try:
        user_id = get_jwt_identity()
        limit = int(request.args.get('limit', 50))
        
        messages = list(
            chat_messages_collection.find({'user_id': user_id})
            .sort('created_at', 1)
            .limit(limit)
        )
        
        return jsonify([serialize_doc(m) for m in messages]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat/messages', methods=['POST'])
@jwt_required()
def save_chat_message():
    """Save a chat message"""
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        message = {
            'user_id': user_id,
            'role': data.get('role', 'user'),
            'content': data.get('content', ''),
            'created_at': datetime.now()
        }
        
        result = chat_messages_collection.insert_one(message)
        message['id'] = str(result.inserted_id)
        del message['_id']
        
        return jsonify(message), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat/messages', methods=['DELETE'])
@jwt_required()
def clear_chat_messages():
    """Clear all chat messages for user"""
    try:
        user_id = get_jwt_identity()
        chat_messages_collection.delete_many({'user_id': user_id})
        return jsonify({'message': 'Chat history cleared'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# HEALTH CHECK
# ============================================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Test MongoDB connection
        client.admin.command('ping')
        return jsonify({
            'status': 'healthy',
            'database': 'MongoDB connected',
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500


# ============================================
# RUN THE APP
# ============================================

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 STOCK PREDICTION API SERVER")
    print("=" * 50)
    print(f"📊 MongoDB: {config.MONGODB_URI}")
    print(f"🔗 Server: http://localhost:{config.PORT}")
    print(f"🌐 CORS: {config.CORS_ORIGINS}")
    print("=" * 50)
    
    app.run(
        debug=config.FLASK_DEBUG,
        host='0.0.0.0',
        port=config.PORT
    )
```

---

# 🎨 FRONTEND FILES

## 1. frontend/.env

```env
VITE_FLASK_API_URL=http://localhost:5000
```

---

## 2. frontend/src/services/api.ts

```typescript
// ============================================
// API SERVICE - MONGODB BACKEND
// ============================================

const API_URL = import.meta.env.VITE_FLASK_API_URL || 'http://localhost:5000';

// Token management
export const getToken = (): string | null => {
  return localStorage.getItem('auth_token');
};

export const setToken = (token: string): void => {
  localStorage.setItem('auth_token', token);
};

export const removeToken = (): void => {
  localStorage.removeItem('auth_token');
};

// API request helper
const apiRequest = async (
  endpoint: string,
  options: RequestInit = {}
): Promise<any> => {
  const token = getToken();
  
  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...options.headers,
  };
  
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers,
  });
  
  const data = await response.json();
  
  if (!response.ok) {
    throw new Error(data.error || 'Request failed');
  }
  
  return data;
};

// ============================================
// AUTH API
// ============================================

export const authApi = {
  signup: async (email: string, password: string, fullName: string) => {
    const data = await apiRequest('/api/auth/signup', {
      method: 'POST',
      body: JSON.stringify({ email, password, full_name: fullName }),
    });
    if (data.access_token) {
      setToken(data.access_token);
    }
    return data;
  },
  
  login: async (email: string, password: string) => {
    const data = await apiRequest('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    if (data.access_token) {
      setToken(data.access_token);
    }
    return data;
  },
  
  logout: async () => {
    try {
      await apiRequest('/api/auth/logout', { method: 'POST' });
    } finally {
      removeToken();
    }
  },
  
  getCurrentUser: async () => {
    return apiRequest('/api/auth/me');
  },
};

// ============================================
// PROFILE API
// ============================================

export const profileApi = {
  getProfile: async () => {
    return apiRequest('/api/profile');
  },
  
  updateProfile: async (data: { full_name?: string; email?: string }) => {
    return apiRequest('/api/profile', {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  },
};

// ============================================
// STOCK API
// ============================================

export const stockApi = {
  getSymbols: async (sector?: string, search?: string) => {
    const params = new URLSearchParams();
    if (sector) params.append('sector', sector);
    if (search) params.append('search', search);
    return apiRequest(`/api/symbols?${params}`);
  },
  
  getSectors: async () => {
    return apiRequest('/api/sectors');
  },
  
  getStockData: async (symbol: string, period: string = '1y') => {
    return apiRequest(`/api/get_stock_data/${symbol}?period=${period}`);
  },
  
  getMultipleStocks: async (symbols: string[]) => {
    return apiRequest('/api/get_multiple_stocks', {
      method: 'POST',
      body: JSON.stringify({ symbols }),
    });
  },
  
  getMarketOverview: async () => {
    return apiRequest('/api/market_overview');
  },
  
  getSectorStocks: async (sector: string, limit: number = 10) => {
    return apiRequest(`/api/get_sector_stocks/${sector}?limit=${limit}`);
  },
  
  searchStocks: async (query: string) => {
    return apiRequest(`/api/search/${query}`);
  },
};

// ============================================
// WATCHLIST API
// ============================================

export const watchlistApi = {
  getWatchlist: async () => {
    return apiRequest('/api/watchlist');
  },
  
  addToWatchlist: async (symbol: string) => {
    return apiRequest('/api/watchlist', {
      method: 'POST',
      body: JSON.stringify({ symbol }),
    });
  },
  
  removeFromWatchlist: async (symbol: string) => {
    return apiRequest(`/api/watchlist/${symbol}`, {
      method: 'DELETE',
    });
  },
};

// ============================================
// PREDICTION API
// ============================================

export const predictionApi = {
  predict: async (
    symbol: string,
    modelType: 'SVM' | 'DecisionTree' | 'RandomForest' = 'RandomForest'
  ) => {
    return apiRequest('/api/predict', {
      method: 'POST',
      body: JSON.stringify({ symbol, model_type: modelType }),
    });
  },
  
  getHistory: async (limit: number = 20) => {
    return apiRequest(`/api/predictions/history?limit=${limit}`);
  },
};

// ============================================
// CHAT API
// ============================================

export const chatApi = {
  getMessages: async (limit: number = 50) => {
    return apiRequest(`/api/chat/messages?limit=${limit}`);
  },
  
  saveMessage: async (role: string, content: string) => {
    return apiRequest('/api/chat/messages', {
      method: 'POST',
      body: JSON.stringify({ role, content }),
    });
  },
  
  clearMessages: async () => {
    return apiRequest('/api/chat/messages', {
      method: 'DELETE',
    });
  },
};

// ============================================
// HEALTH CHECK
// ============================================

export const checkBackendHealth = async (): Promise<boolean> => {
  try {
    const response = await fetch(`${API_URL}/health`);
    return response.ok;
  } catch {
    return false;
  }
};
```

---

## 3. frontend/src/contexts/AuthContext.tsx

```typescript
// ============================================
// AUTH CONTEXT - MONGODB BASED
// ============================================

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { authApi, getToken, removeToken } from '@/services/api';

interface User {
  id: string;
  email: string;
  full_name: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, fullName: string) => Promise<void>;
  logout: () => Promise<void>;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    const token = getToken();
    if (!token) {
      setLoading(false);
      return;
    }

    try {
      const data = await authApi.getCurrentUser();
      setUser(data.user);
    } catch (error) {
      console.error('Auth check failed:', error);
      removeToken();
    } finally {
      setLoading(false);
    }
  };

  const login = async (email: string, password: string) => {
    const data = await authApi.login(email, password);
    setUser(data.user);
  };

  const signup = async (email: string, password: string, fullName: string) => {
    const data = await authApi.signup(email, password, fullName);
    setUser(data.user);
  };

  const logout = async () => {
    await authApi.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        signup,
        logout,
        isAuthenticated: !!user,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
```

---

## 4. frontend/src/App.tsx

```typescript
import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "@/contexts/AuthContext";

// Pages
import Index from "./pages/Index";
import Auth from "./pages/Auth";
import Dashboard from "./pages/Dashboard";
import Profile from "./pages/Profile";
import Chat from "./pages/Chat";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

// Protected Route Component
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/auth" replace />;
  }

  return <>{children}</>;
};

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/auth" element={<Auth />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="/profile"
        element={
          <ProtectedRoute>
            <Profile />
          </ProtectedRoute>
        }
      />
      <Route
        path="/chat"
        element={
          <ProtectedRoute>
            <Chat />
          </ProtectedRoute>
        }
      />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

const App = () => (
  <QueryClientProvider client={queryClient}>
    <AuthProvider>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <AppRoutes />
        </BrowserRouter>
      </TooltipProvider>
    </AuthProvider>
  </QueryClientProvider>
);

export default App;
```

---

## 5. frontend/src/pages/Auth.tsx

```typescript
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { useToast } from '@/hooks/use-toast';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

const Auth = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [loading, setLoading] = useState(false);
  const { login, signup } = useAuth();
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      await login(email, password);
      toast({ title: 'Welcome back!', description: 'Successfully logged in.' });
      navigate('/dashboard');
    } catch (error: any) {
      toast({
        title: 'Login failed',
        description: error.message || 'Invalid credentials',
        variant: 'destructive',
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      await signup(email, password, fullName);
      toast({ title: 'Account created!', description: 'Welcome to Stock Predictor.' });
      navigate('/dashboard');
    } catch (error: any) {
      toast({
        title: 'Signup failed',
        description: error.message || 'Could not create account',
        variant: 'destructive',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl">Stock Predictor</CardTitle>
          <CardDescription>ML-Powered Stock Predictions</CardDescription>
        </CardHeader>
        <CardContent>
          <Tabs defaultValue="login">
            <TabsList className="grid w-full grid-cols-2">
              <TabsTrigger value="login">Login</TabsTrigger>
              <TabsTrigger value="signup">Sign Up</TabsTrigger>
            </TabsList>
            
            <TabsContent value="login">
              <form onSubmit={handleLogin} className="space-y-4 mt-4">
                <Input
                  type="email"
                  placeholder="Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
                <Input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
                <Button type="submit" className="w-full" disabled={loading}>
                  {loading ? 'Logging in...' : 'Login'}
                </Button>
              </form>
            </TabsContent>
            
            <TabsContent value="signup">
              <form onSubmit={handleSignup} className="space-y-4 mt-4">
                <Input
                  type="text"
                  placeholder="Full Name"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  required
                />
                <Input
                  type="email"
                  placeholder="Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
                <Input
                  type="password"
                  placeholder="Password (min 6 characters)"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  minLength={6}
                  required
                />
                <Button type="submit" className="w-full" disabled={loading}>
                  {loading ? 'Creating account...' : 'Create Account'}
                </Button>
              </form>
            </TabsContent>
          </Tabs>
        </CardContent>
      </Card>
    </div>
  );
};

export default Auth;
```

---

## 6. frontend/src/components/Navbar.tsx

```typescript
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';
import { Button } from '@/components/ui/button';
import { useToast } from '@/hooks/use-toast';
import { TrendingUp, User, LogOut, MessageSquare, LayoutDashboard } from 'lucide-react';

const Navbar = () => {
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleLogout = async () => {
    try {
      await logout();
      toast({ title: 'Logged out', description: 'See you next time!' });
      navigate('/');
    } catch (error) {
      toast({ title: 'Error', description: 'Failed to logout', variant: 'destructive' });
    }
  };

  return (
    <nav className="bg-card border-b border-border">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2">
            <TrendingUp className="h-6 w-6 text-primary" />
            <span className="font-bold text-xl">StockPredictor</span>
          </Link>

          {/* Navigation Links */}
          <div className="flex items-center gap-4">
            {isAuthenticated ? (
              <>
                <Link to="/dashboard">
                  <Button variant="ghost" size="sm">
                    <LayoutDashboard className="h-4 w-4 mr-2" />
                    Dashboard
                  </Button>
                </Link>
                <Link to="/chat">
                  <Button variant="ghost" size="sm">
                    <MessageSquare className="h-4 w-4 mr-2" />
                    AI Chat
                  </Button>
                </Link>
                <Link to="/profile">
                  <Button variant="ghost" size="sm">
                    <User className="h-4 w-4 mr-2" />
                    Profile
                  </Button>
                </Link>
                <Button variant="outline" size="sm" onClick={handleLogout}>
                  <LogOut className="h-4 w-4 mr-2" />
                  Logout
                </Button>
              </>
            ) : (
              <Link to="/auth">
                <Button>Get Started</Button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

---

## 7. frontend/src/pages/Dashboard.tsx

```typescript
import React, { useState, useEffect } from 'react';
import Navbar from '@/components/Navbar';
import { useAuth } from '@/contexts/AuthContext';
import { stockApi, watchlistApi, predictionApi } from '@/services/api';
import { useToast } from '@/hooks/use-toast';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { TrendingUp, TrendingDown, Plus, Trash2, Search, Brain } from 'lucide-react';

interface WatchlistItem {
  id: string;
  symbol: string;
  company_name: string;
  current_price?: number;
  change_percent?: number;
}

interface Prediction {
  symbol: string;
  predicted_price: number;
  current_price: number;
  confidence: number;
  model_type: string;
}

const Dashboard = () => {
  const { user } = useAuth();
  const { toast } = useToast();
  
  const [watchlist, setWatchlist] = useState<WatchlistItem[]>([]);
  const [searchSymbol, setSearchSymbol] = useState('');
  const [selectedSymbol, setSelectedSymbol] = useState('');
  const [modelType, setModelType] = useState<'RandomForest' | 'SVM' | 'DecisionTree'>('RandomForest');
  const [prediction, setPrediction] = useState<Prediction | null>(null);
  const [loading, setLoading] = useState(false);
  const [predicting, setPredicting] = useState(false);

  useEffect(() => {
    loadWatchlist();
  }, []);

  const loadWatchlist = async () => {
    try {
      setLoading(true);
      const data = await watchlistApi.getWatchlist();
      setWatchlist(data);
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    } finally {
      setLoading(false);
    }
  };

  const handleAddToWatchlist = async () => {
    if (!searchSymbol.trim()) return;
    
    try {
      await watchlistApi.addToWatchlist(searchSymbol.toUpperCase());
      toast({ title: 'Success', description: `${searchSymbol.toUpperCase()} added to watchlist` });
      setSearchSymbol('');
      loadWatchlist();
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    }
  };

  const handleRemoveFromWatchlist = async (symbol: string) => {
    try {
      await watchlistApi.removeFromWatchlist(symbol);
      toast({ title: 'Removed', description: `${symbol} removed from watchlist` });
      loadWatchlist();
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    }
  };

  const handlePredict = async () => {
    if (!selectedSymbol) {
      toast({ title: 'Error', description: 'Please select a stock', variant: 'destructive' });
      return;
    }
    
    try {
      setPredicting(true);
      const result = await predictionApi.predict(selectedSymbol, modelType);
      setPrediction(result);
      toast({ title: 'Prediction Complete', description: `${selectedSymbol} analyzed with ${modelType}` });
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    } finally {
      setPredicting(false);
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">
          Welcome back, {user?.full_name || 'Trader'}!
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Watchlist Section */}
          <Card className="lg:col-span-2">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <TrendingUp className="h-5 w-5" />
                Your Watchlist
              </CardTitle>
            </CardHeader>
            <CardContent>
              {/* Add to Watchlist */}
              <div className="flex gap-2 mb-6">
                <Input
                  placeholder="Enter stock symbol (e.g., AAPL)"
                  value={searchSymbol}
                  onChange={(e) => setSearchSymbol(e.target.value.toUpperCase())}
                  className="flex-1"
                />
                <Button onClick={handleAddToWatchlist}>
                  <Plus className="h-4 w-4 mr-2" />
                  Add
                </Button>
              </div>

              {/* Watchlist Items */}
              {loading ? (
                <p className="text-muted-foreground">Loading...</p>
              ) : watchlist.length === 0 ? (
                <p className="text-muted-foreground">No stocks in watchlist. Add some to get started!</p>
              ) : (
                <div className="space-y-3">
                  {watchlist.map((item) => (
                    <div
                      key={item.id}
                      className="flex items-center justify-between p-4 bg-muted/50 rounded-lg cursor-pointer hover:bg-muted transition-colors"
                      onClick={() => setSelectedSymbol(item.symbol)}
                    >
                      <div>
                        <p className="font-semibold">{item.symbol}</p>
                        <p className="text-sm text-muted-foreground">{item.company_name}</p>
                      </div>
                      <div className="flex items-center gap-4">
                        {item.current_price && (
                          <div className="text-right">
                            <p className="font-medium">${item.current_price.toFixed(2)}</p>
                            <p className={`text-sm flex items-center ${
                              (item.change_percent || 0) >= 0 ? 'text-green-500' : 'text-red-500'
                            }`}>
                              {(item.change_percent || 0) >= 0 ? (
                                <TrendingUp className="h-3 w-3 mr-1" />
                              ) : (
                                <TrendingDown className="h-3 w-3 mr-1" />
                              )}
                              {Math.abs(item.change_percent || 0).toFixed(2)}%
                            </p>
                          </div>
                        )}
                        <Button
                          variant="ghost"
                          size="sm"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleRemoveFromWatchlist(item.symbol);
                          }}
                        >
                          <Trash2 className="h-4 w-4 text-destructive" />
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>

          {/* Prediction Section */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Brain className="h-5 w-5" />
                ML Prediction
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <label className="text-sm font-medium mb-2 block">Stock Symbol</label>
                <Input
                  placeholder="e.g., AAPL"
                  value={selectedSymbol}
                  onChange={(e) => setSelectedSymbol(e.target.value.toUpperCase())}
                />
              </div>

              <div>
                <label className="text-sm font-medium mb-2 block">ML Model</label>
                <Select value={modelType} onValueChange={(v) => setModelType(v as any)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="RandomForest">Random Forest</SelectItem>
                    <SelectItem value="SVM">Support Vector Machine</SelectItem>
                    <SelectItem value="DecisionTree">Decision Tree</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Button
                className="w-full"
                onClick={handlePredict}
                disabled={predicting || !selectedSymbol}
              >
                {predicting ? 'Analyzing...' : 'Get Prediction'}
              </Button>

              {prediction && (
                <div className="mt-6 p-4 bg-muted rounded-lg">
                  <h3 className="font-semibold text-lg mb-3">{prediction.symbol} Prediction</h3>
                  <div className="space-y-2">
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Current Price:</span>
                      <span className="font-medium">${prediction.current_price.toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Predicted Price:</span>
                      <span className={`font-bold ${
                        prediction.predicted_price > prediction.current_price
                          ? 'text-green-500'
                          : 'text-red-500'
                      }`}>
                        ${prediction.predicted_price.toFixed(2)}
                      </span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Confidence:</span>
                      <span className="font-medium">{(prediction.confidence * 100).toFixed(1)}%</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Model:</span>
                      <span className="font-medium">{prediction.model_type}</span>
                    </div>
                  </div>
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
```

---

## 8. frontend/src/pages/Profile.tsx

```typescript
import React, { useState, useEffect } from 'react';
import Navbar from '@/components/Navbar';
import { useAuth } from '@/contexts/AuthContext';
import { profileApi, predictionApi } from '@/services/api';
import { useToast } from '@/hooks/use-toast';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { User, History } from 'lucide-react';

interface PredictionHistory {
  id: string;
  symbol: string;
  predicted_price: number;
  current_price: number;
  confidence: number;
  model_type: string;
  created_at: string;
}

const Profile = () => {
  const { user } = useAuth();
  const { toast } = useToast();
  
  const [fullName, setFullName] = useState(user?.full_name || '');
  const [email, setEmail] = useState(user?.email || '');
  const [updating, setUpdating] = useState(false);
  const [predictions, setPredictions] = useState<PredictionHistory[]>([]);

  useEffect(() => {
    loadPredictionHistory();
  }, []);

  const loadPredictionHistory = async () => {
    try {
      const data = await predictionApi.getHistory(10);
      setPredictions(data);
    } catch (error) {
      console.error('Failed to load prediction history:', error);
    }
  };

  const handleUpdateProfile = async (e: React.FormEvent) => {
    e.preventDefault();
    setUpdating(true);
    
    try {
      await profileApi.updateProfile({ full_name: fullName, email });
      toast({ title: 'Profile Updated', description: 'Your profile has been updated successfully.' });
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    } finally {
      setUpdating(false);
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Profile Settings</h1>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Profile Card */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <User className="h-5 w-5" />
                Your Profile
              </CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleUpdateProfile} className="space-y-4">
                <div>
                  <label className="text-sm font-medium mb-2 block">Full Name</label>
                  <Input
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    placeholder="Enter your full name"
                  />
                </div>
                <div>
                  <label className="text-sm font-medium mb-2 block">Email</label>
                  <Input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                  />
                </div>
                <Button type="submit" disabled={updating}>
                  {updating ? 'Updating...' : 'Update Profile'}
                </Button>
              </form>
            </CardContent>
          </Card>

          {/* Prediction History */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <History className="h-5 w-5" />
                Recent Predictions
              </CardTitle>
            </CardHeader>
            <CardContent>
              {predictions.length === 0 ? (
                <p className="text-muted-foreground">No predictions yet.</p>
              ) : (
                <div className="space-y-3">
                  {predictions.map((pred) => (
                    <div key={pred.id} className="p-3 bg-muted/50 rounded-lg">
                      <div className="flex justify-between items-start">
                        <div>
                          <p className="font-semibold">{pred.symbol}</p>
                          <p className="text-sm text-muted-foreground">{pred.model_type}</p>
                        </div>
                        <div className="text-right">
                          <p className={`font-medium ${
                            pred.predicted_price > pred.current_price
                              ? 'text-green-500'
                              : 'text-red-500'
                          }`}>
                            ${pred.predicted_price.toFixed(2)}
                          </p>
                          <p className="text-sm text-muted-foreground">
                            {(pred.confidence * 100).toFixed(0)}% confidence
                          </p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
};

export default Profile;
```

---

## 9. frontend/src/pages/Chat.tsx

```typescript
import React, { useState, useEffect, useRef } from 'react';
import Navbar from '@/components/Navbar';
import { useAuth } from '@/contexts/AuthContext';
import { chatApi } from '@/services/api';
import { useToast } from '@/hooks/use-toast';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Send, Bot, User, Trash2 } from 'lucide-react';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  created_at: string;
}

const Chat = () => {
  const { user } = useAuth();
  const { toast } = useToast();
  
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    loadMessages();
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  const loadMessages = async () => {
    try {
      const data = await chatApi.getMessages();
      setMessages(data);
    } catch (error) {
      console.error('Failed to load messages:', error);
    }
  };

  const handleSend = async () => {
    if (!input.trim()) return;
    
    const userMessage = input.trim();
    setInput('');
    setLoading(true);

    try {
      // Save user message
      const savedUserMsg = await chatApi.saveMessage('user', userMessage);
      setMessages((prev) => [...prev, savedUserMsg]);

      // Simulate AI response (replace with actual AI API)
      const aiResponse = generateMockResponse(userMessage);
      const savedAiMsg = await chatApi.saveMessage('assistant', aiResponse);
      setMessages((prev) => [...prev, savedAiMsg]);
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    } finally {
      setLoading(false);
    }
  };

  const handleClearChat = async () => {
    try {
      await chatApi.clearMessages();
      setMessages([]);
      toast({ title: 'Chat Cleared', description: 'All messages have been deleted.' });
    } catch (error: any) {
      toast({ title: 'Error', description: error.message, variant: 'destructive' });
    }
  };

  const generateMockResponse = (question: string): string => {
    const q = question.toLowerCase();
    if (q.includes('predict') || q.includes('price')) {
      return "To get a stock prediction, go to the Dashboard and use the ML Prediction feature. You can choose from Random Forest, SVM, or Decision Tree models.";
    }
    if (q.includes('watchlist')) {
      return "You can add stocks to your watchlist from the Dashboard. Just enter a stock symbol and click 'Add'. Your watchlist will show real-time prices!";
    }
    if (q.includes('model') || q.includes('algorithm')) {
      return "We offer three ML models:\n\n1. **Random Forest** - Best for general predictions\n2. **SVM** - Good for complex patterns\n3. **Decision Tree** - Fast and interpretable";
    }
    return "I'm your Stock AI Assistant! I can help you with:\n- Stock predictions\n- Watchlist management\n- Understanding ML models\n\nWhat would you like to know?";
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      <main className="container mx-auto px-4 py-8">
        <Card className="max-w-3xl mx-auto h-[600px] flex flex-col">
          <CardHeader className="flex-row justify-between items-center">
            <CardTitle className="flex items-center gap-2">
              <Bot className="h-5 w-5" />
              AI Stock Assistant
            </CardTitle>
            <Button variant="ghost" size="sm" onClick={handleClearChat}>
              <Trash2 className="h-4 w-4 mr-2" />
              Clear
            </Button>
          </CardHeader>
          
          <CardContent className="flex-1 flex flex-col overflow-hidden">
            <ScrollArea className="flex-1 pr-4" ref={scrollRef}>
              {messages.length === 0 ? (
                <div className="text-center text-muted-foreground py-8">
                  <Bot className="h-12 w-12 mx-auto mb-4 opacity-50" />
                  <p>Start a conversation with your AI assistant!</p>
                </div>
              ) : (
                <div className="space-y-4">
                  {messages.map((msg) => (
                    <div
                      key={msg.id}
                      className={`flex gap-3 ${
                        msg.role === 'user' ? 'justify-end' : 'justify-start'
                      }`}
                    >
                      {msg.role === 'assistant' && (
                        <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
                          <Bot className="h-4 w-4 text-primary" />
                        </div>
                      )}
                      <div
                        className={`max-w-[80%] p-3 rounded-lg ${
                          msg.role === 'user'
                            ? 'bg-primary text-primary-foreground'
                            : 'bg-muted'
                        }`}
                      >
                        <p className="whitespace-pre-wrap">{msg.content}</p>
                      </div>
                      {msg.role === 'user' && (
                        <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                          <User className="h-4 w-4 text-primary-foreground" />
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </ScrollArea>

            <div className="flex gap-2 mt-4 pt-4 border-t">
              <Input
                placeholder="Ask about stocks, predictions, or trading..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                disabled={loading}
              />
              <Button onClick={handleSend} disabled={loading || !input.trim()}>
                <Send className="h-4 w-4" />
              </Button>
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default Chat;
```

---

## 10. frontend/package.json

```json
{
  "name": "stock-prediction-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-dropdown-menu": "^2.1.15",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-scroll-area": "^1.2.9",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-tabs": "^1.1.12",
    "@radix-ui/react-toast": "^1.2.14",
    "@radix-ui/react-tooltip": "^1.2.7",
    "@tanstack/react-query": "^5.83.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.462.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.61.1",
    "react-router-dom": "^6.30.1",
    "recharts": "^2.15.4",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.0",
    "tailwindcss-animate": "^1.0.7",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/react": "^18.3.1",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.5.3",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.8.3",
    "vite": "^6.0.5"
  }
}
```

---

# 🗄️ MONGODB COLLECTIONS

## Collection Schemas

### 1. users
```javascript
{
  _id: ObjectId,
  email: String (unique),
  password_hash: Binary,
  created_at: Date,
  updated_at: Date
}
```

### 2. profiles
```javascript
{
  _id: ObjectId,
  user_id: String,
  email: String,
  full_name: String,
  created_at: Date,
  updated_at: Date
}
```

### 3. watchlist
```javascript
{
  _id: ObjectId,
  user_id: String,
  symbol: String,
  company_name: String,
  added_at: Date
}
// Index: { user_id: 1, symbol: 1 } (unique)
```

### 4. stock_data
```javascript
{
  _id: ObjectId,
  symbol: String,
  name: String,
  current_price: Number,
  change: Number,
  change_percent: Number,
  history: Array,
  fetched_at: Date
}
```

### 5. stock_predictions
```javascript
{
  _id: ObjectId,
  user_id: String,
  symbol: String,
  predicted_price: Number,
  current_price: Number,
  confidence: Number,
  model_type: String,
  prediction_date: Date,
  created_at: Date
}
```

### 6. chat_messages
```javascript
{
  _id: ObjectId,
  user_id: String,
  role: String, // 'user' or 'assistant'
  content: String,
  created_at: Date
}
```

---

# 🚀 QUICK START GUIDE

## Step 1: Start MongoDB
```bash
# Make sure MongoDB is running
mongod --dbpath /path/to/data
```

## Step 2: Setup Backend
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "MONGODB_URI=mongodb://localhost:27017/stockDB" > .env
echo "JWT_SECRET_KEY=your-secret-key-here" >> .env

# Run the server
python app.py
```

## Step 3: Setup Frontend
```bash
cd frontend

# Install dependencies
npm install

# Create .env file
echo "VITE_FLASK_API_URL=http://localhost:5000" > .env

# Run development server
npm run dev
```

## Step 4: Access the App
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000
- Health Check: http://localhost:5000/health

---

# 📡 API ENDPOINTS SUMMARY

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/api/auth/signup` | POST | No | Register new user |
| `/api/auth/login` | POST | No | Login user |
| `/api/auth/me` | GET | Yes | Get current user |
| `/api/auth/logout` | POST | Yes | Logout |
| `/api/profile` | GET/PUT | Yes | Profile CRUD |
| `/api/symbols` | GET | No | Get stock symbols |
| `/api/sectors` | GET | No | Get sectors |
| `/api/get_stock_data/<symbol>` | GET | No | Get stock data |
| `/api/market_overview` | GET | No | Market overview |
| `/api/watchlist` | GET/POST | Yes | Watchlist CRUD |
| `/api/watchlist/<symbol>` | DELETE | Yes | Remove from watchlist |
| `/api/predict` | POST | Optional | ML prediction |
| `/api/predictions/history` | GET | Yes | Prediction history |
| `/api/chat/messages` | GET/POST/DELETE | Yes | Chat messages |
| `/health` | GET | No | Health check |

---

This is your complete fresh repository with MongoDB integration! 🎉
