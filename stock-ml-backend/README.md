# Stock ML Backend

Flask backend for stock prediction using machine learning models (SVM, Decision Tree, Random Forest, LSTM).

## Database Setup

The backend connects to your Lovable Cloud database automatically. No additional database setup required!

## Setup Instructions

### 1. Install Python
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Mac**: `brew install python3`
- **Linux**: `sudo apt-get install python3 python3-pip`

### 2. Install Dependencies

```bash
cd stock-ml-backend
pip install -r requirements.txt
```

### 3. Run Locally

```bash
python app.py
```

Backend will run on `http://localhost:5000`

### 4. Test the API

**Get Stock Data:**
```bash
curl http://localhost:5000/api/get_stock_data/AAPL
```

**Get Prediction:**
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL", "user_id": "your-user-id", "model_type": "RandomForest"}'
```

## Production Deployment

### Option 1: Heroku
```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### Option 2: Railway.app
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Deploy automatically

### Option 3: Render.com
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect repository
4. Deploy

## API Endpoints

### GET `/api/get_stock_data/<symbol>`
Fetches stock data from Yahoo Finance and saves to database.

**Response:**
```json
{
  "symbol": "AAPL",
  "data": [...],
  "current_price": 150.25
}
```

### POST `/api/predict`
Runs ML prediction and saves to database.

**Request Body:**
```json
{
  "symbol": "AAPL",
  "user_id": "uuid",
  "model_type": "RandomForest"
}
```

**Response:**
```json
{
  "symbol": "AAPL",
  "predicted_price": 155.50,
  "current_price": 150.25,
  "model_type": "RandomForest",
  "confidence": 87.5
}
```

## Environment Variables (Production)

No environment variables needed - database credentials are included in the code.

## Model Types

- **SVM**: Support Vector Machine
- **DecisionTree**: Decision Tree Regressor
- **RandomForest**: Random Forest Regressor (default)
- **LSTM**: Long Short-Term Memory Neural Network
