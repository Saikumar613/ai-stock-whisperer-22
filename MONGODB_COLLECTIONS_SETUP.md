# MongoDB Collections Setup Guide

## Important: Collections are Created Automatically!

**You do NOT need to manually create collections or insert JSON/CSV files.** MongoDB creates collections automatically when you first insert data through the Flask API.

---

## How It Works

1. **Start MongoDB** - Just ensure MongoDB is running
2. **Start Flask Backend** - The app connects to `mongodb://localhost:27017/stockDB`
3. **Use the App** - Collections are created automatically when you:
   - Sign up (creates `users` collection)
   - Add stocks to watchlist (creates `watchlist` collection)
   - Fetch stock data (creates `stock_data` collection)
   - Run predictions (creates `stock_predictions` collection)
   - Use AI chat (creates `chat_messages` collection)

---

## If You Want to Manually Create Collections (Optional)

### Method 1: Using MongoDB Shell (mongosh)

```bash
# Connect to MongoDB
mongosh mongodb://localhost:27017/stockDB

# Create collections with validation (optional)
db.createCollection("users")
db.createCollection("profiles")
db.createCollection("watchlist")
db.createCollection("stock_data")
db.createCollection("stock_predictions")
db.createCollection("chat_messages")

# Verify collections exist
show collections
```

### Method 2: Using MongoDB Compass (GUI)

1. Download and install [MongoDB Compass](https://www.mongodb.com/products/compass)
2. Connect to: `mongodb://localhost:27017`
3. Click "Create Database" → Name: `stockDB`
4. Add collections one by one (click the + button)

---

## Collection Schemas (For Reference Only)

### users
```javascript
{
  "_id": ObjectId,
  "email": "user@example.com",
  "password_hash": "bcrypt_hashed_password",
  "full_name": "John Doe",
  "created_at": ISODate("2024-01-01T00:00:00Z")
}
```

### profiles
```javascript
{
  "_id": ObjectId,
  "user_id": ObjectId,  // References users._id
  "email": "user@example.com",
  "full_name": "John Doe",
  "avatar_url": "https://...",
  "created_at": ISODate,
  "updated_at": ISODate
}
```

### watchlist
```javascript
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "symbol": "AAPL",
  "company_name": "Apple Inc.",
  "added_at": ISODate
}
```

### stock_data
```javascript
{
  "_id": ObjectId,
  "symbol": "AAPL",
  "data": [
    {
      "Date": "2024-01-01",
      "Open": 150.0,
      "High": 155.0,
      "Low": 149.0,
      "Close": 154.0,
      "Volume": 1000000
    }
  ],
  "last_updated": ISODate
}
```

### stock_predictions
```javascript
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "symbol": "AAPL",
  "model_type": "RandomForest",
  "predicted_price": 175.50,
  "current_price": 170.00,
  "confidence": 85.5,
  "prediction_date": ISODate,
  "created_at": ISODate
}
```

### chat_messages
```javascript
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "role": "user" | "assistant",
  "content": "What's the outlook for AAPL?",
  "created_at": ISODate
}
```

---

## Common Errors and Solutions

### Error: "Document failed validation"
**Cause:** You're trying to insert data that doesn't match expected format.
**Solution:** Don't manually insert data. Let the Flask API handle it.

### Error: "E11000 duplicate key error"
**Cause:** Trying to insert a document with a duplicate `_id` or unique field.
**Solution:** Remove the `_id` field from your JSON, MongoDB generates it automatically.

### Error: "Invalid JSON"
**Cause:** JSON format issues when importing.
**Solution:** Use proper JSON format (double quotes, no trailing commas):
```json
{
  "email": "test@example.com",
  "full_name": "Test User"
}
```

### Error: "Cannot insert CSV directly"
**Cause:** MongoDB doesn't accept CSV files directly.
**Solution:** Use `mongoimport` with `--type csv`:
```bash
mongoimport --db stockDB --collection stock_data --type csv --headerline --file data.csv
```

---

## Insert Sample Data (Optional)

If you want to insert sample data for testing:

```bash
# Using mongosh
mongosh mongodb://localhost:27017/stockDB

# Insert a sample user (password: "password123")
db.users.insertOne({
  email: "test@example.com",
  password_hash: "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.G/lKfsmTB4Omvy",
  full_name: "Test User",
  created_at: new Date()
})

# Insert sample watchlist item
db.watchlist.insertOne({
  user_id: db.users.findOne({email: "test@example.com"})._id,
  symbol: "AAPL",
  company_name: "Apple Inc.",
  added_at: new Date()
})
```

---

## Verify Your Setup

```bash
# Connect to MongoDB
mongosh mongodb://localhost:27017/stockDB

# Check all collections
show collections

# Check users
db.users.find().pretty()

# Check watchlist
db.watchlist.find().pretty()

# Check stock data
db.stock_data.find().pretty()

# Check predictions
db.stock_predictions.find().pretty()
```

---

## Quick Start Checklist

- [ ] MongoDB is running (`mongod` or MongoDB service)
- [ ] Flask backend is running (`python app.py`)
- [ ] Frontend is running (`npm run dev`)
- [ ] Sign up through the app (creates user automatically)
- [ ] Add stocks to watchlist (creates data automatically)
- [ ] Run predictions (stores results automatically)

**That's it! No manual collection setup needed.**
