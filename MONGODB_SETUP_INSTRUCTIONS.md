# 🚀 COMPLETE SETUP INSTRUCTIONS - Stock Prediction App

## 📋 WHAT YOU NEED TO INSTALL

### 1. **Node.js** (for Frontend)
- Download: https://nodejs.org/
- Version: 18 or higher
- This runs the React app

### 2. **Python** (for Backend)
- Download: https://www.python.org/
- Version: 3.8 or higher
- This runs the Flask API

### 3. **MongoDB** (for Database)
- Download: https://www.mongodb.com/try/download/community
- Or use MongoDB Atlas (free cloud database): https://www.mongodb.com/cloud/atlas

---

## 🗂️ PROJECT STRUCTURE

```
stock-prediction-app/
│
├── frontend/              → React App (This Lovable project)
│   ├── src/
│   ├── package.json
│   └── node_modules/
│
├── backend/               → Flask API (Create this folder)
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
└── MongoDB Database       → Running locally or on MongoDB Atlas
```

---

## ⚙️ STEP-BY-STEP SETUP

### **STEP 1: Install MongoDB**

#### Option A: Local MongoDB (Recommended for beginners)
1. Download MongoDB Community Edition
2. Install it (keep default settings)
3. MongoDB will run on: `mongodb://localhost:27017`

#### Option B: MongoDB Atlas (Cloud - Free)
1. Go to https://www.mongodb.com/cloud/atlas
2. Create free account
3. Create a free cluster
4. Get your connection string (looks like: `mongodb+srv://username:password@cluster.mongodb.net/`)

---

### **STEP 2: Setup Backend (Flask + Python)**

#### 2.1 Create backend folder
Open Terminal/Command Prompt:
```bash
mkdir backend
cd backend
```

#### 2.2 Create app.py file
(See backend/app.py code below)

#### 2.3 Create requirements.txt file
(See backend/requirements.txt code below)

#### 2.4 Create .env file
```bash
# Create .env file in backend folder
MONGODB_URI=mongodb://localhost:27017/stock_prediction
# OR if using MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/stock_prediction
```

#### 2.5 Install Python packages
```bash
# Make sure you're in backend folder
pip install -r requirements.txt
```

#### 2.6 Run the backend
```bash
python app.py
```

✅ Backend will run on: `http://localhost:5000`

---

### **STEP 3: Setup Frontend (React)**

#### 3.1 Add environment variable
Create `.env` file in the frontend (root) folder:
```
VITE_FLASK_API_URL=http://localhost:5000
```

#### 3.2 Install dependencies
Open Terminal in the frontend folder:
```bash
npm install
```

#### 3.3 Run the frontend
```bash
npm run dev
```

✅ Frontend will run on: `http://localhost:8080`

---

## 🎯 HOW TO USE THE APP

1. **Start MongoDB** (if local, it should auto-start)
2. **Start Backend**: 
   - Open Terminal in `backend/` folder
   - Run: `python app.py`
   - Keep this terminal open
3. **Start Frontend**:
   - Open NEW Terminal in frontend folder
   - Run: `npm run dev`
   - Keep this terminal open
4. **Open Browser**: Go to `http://localhost:8080`

---

## 📂 FOLDER LOCATIONS

| Component | Folder | Tool to Open | Command to Run |
|-----------|--------|--------------|----------------|
| **Frontend** | Root folder (this project) | VS Code / Lovable | `npm run dev` |
| **Backend** | `backend/` subfolder | VS Code / Python IDE | `python app.py` |
| **Database** | MongoDB installation | MongoDB Compass | Auto-runs |

---

## ✅ VERIFICATION CHECKLIST

- [ ] Node.js installed (`node --version` in terminal)
- [ ] Python installed (`python --version` in terminal)
- [ ] MongoDB installed and running
- [ ] Backend packages installed (`pip install -r requirements.txt`)
- [ ] Frontend packages installed (`npm install`)
- [ ] Backend running on port 5000
- [ ] Frontend running on port 8080
- [ ] Can access app in browser

---

## 🆘 COMMON ISSUES

### "pip not found"
- Make sure Python is installed
- Try `python -m pip` instead of `pip`

### "npm not found"
- Install Node.js from nodejs.org
- Restart terminal after installation

### "MongoDB connection failed"
- Check if MongoDB is running
- Verify MONGODB_URI in .env file
- For Atlas, check username/password

### "Port already in use"
- Stop other apps using port 5000 or 8080
- Or change the port in the code

---

## 📝 ABOUT TYPESCRIPT

The frontend uses TypeScript (`.tsx` files), but:
- It works exactly like JavaScript
- You don't need to learn TypeScript to use it
- The code is the same, just with type hints
- Lovable projects require TypeScript (cannot be changed)

**Don't worry!** If you know React with JavaScript, you already know 95% of what you need.

---

## 🎓 NEXT STEPS

1. Follow STEP 1, 2, 3 above
2. Open the app in browser
3. Search for a stock (e.g., "AAPL")
4. Click "Predict" to see ML predictions
5. Data will be saved in MongoDB

Need help? Read the error messages in the terminal carefully - they usually tell you exactly what's wrong!
