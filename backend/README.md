# 🐍 Stock Prediction Backend - MongoDB Version

Flask API for stock data fetching and ML predictions, storing data in MongoDB.

---

## 📦 INSTALLATION

### 1. Install Python (if not installed)
- Download from: https://www.python.org/
- Version required: 3.8 or higher

### 2. Install MongoDB
- **Local**: Download from https://www.mongodb.com/try/download/community
- **Cloud**: Use MongoDB Atlas (free tier): https://www.mongodb.com/cloud/atlas

### 3. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

---

## ⚙️ CONFIGURATION

Create a `.env` file in the `backend/` folder:

```env
# For local MongoDB
MONGODB_URI=mongodb://localhost:27017/stock_prediction

# For MongoDB Atlas
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/stock_prediction
```

---

## 🚀 RUNNING THE BACKEND

### Start the server:
```bash
python app.py
```

The API will run on: **http://localhost:5000**

---

## 📡 API ENDPOINTS

### 1. Get Stock Data
```http
GET /api/get_stock_data/<symbol>
```

Example:
```bash
curl http://localhost:5000/api/get_stock_data/AAPL
```

Response:
```json
{
  "symbol": "AAPL",
  "current_price": 178.25,
  "history": [...]
}
```

### 2. Predict Stock Price
```http
POST /api/predict
```

Request Body:
```json
{
  "symbol": "AAPL",
  "user_id": "user123",
  "model_type": "RandomForest"
}
```

Model Types: `SVM`, `DecisionTree`, `RandomForest`, `LSTM`

Response:
```json
{
  "predicted_price": 180.50,
  "current_price": 178.25,
  "confidence": 0.89,
  "model_type": "RandomForest",
  "symbol": "AAPL"
}
```

### 3. Health Check
```http
GET /health
```

---

## 🗄️ MONGODB COLLECTIONS

### stock_data
Stores historical stock data:
```json
{
  "_id": ObjectId,
  "symbol": "AAPL",
  "data": [...],
  "created_at": ISODate
}
```

### stock_predictions
Stores ML predictions:
```json
{
  "_id": ObjectId,
  "symbol": "AAPL",
  "user_id": "user123",
  "predicted_price": 180.50,
  "current_price": 178.25,
  "confidence": 0.89,
  "model_type": "RandomForest",
  "created_at": ISODate
}
```

---

## 🔧 TROUBLESHOOTING

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "MongoDB connection failed"
- Check if MongoDB is running (local)
- Verify connection string in `.env`
- For Atlas: Check username/password and network access

### "Port 5000 already in use"
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 📊 TESTING

Test the API:
```bash
# Health check
curl http://localhost:5000/health

# Get stock data
curl http://localhost:5000/api/get_stock_data/AAPL

# Predict stock price
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"symbol":"AAPL","user_id":"test","model_type":"RandomForest"}'
```

---

## 🚀 DEPLOYMENT

### Heroku
```bash
git add .
git commit -m "MongoDB backend"
git push heroku main
```

### Railway.app
1. Connect GitHub repo
2. Add environment variable: `MONGODB_URI`
3. Deploy automatically

---

## 📝 NOTES

- All stock data and predictions are stored in MongoDB
- The backend runs independently of the frontend
- Make sure MongoDB is running before starting the backend
- Use MongoDB Compass to view your database visually
