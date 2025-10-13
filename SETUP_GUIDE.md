# 📚 Complete Setup Guide - Stock Prediction App

## 📁 Project Structure

```
stock-prediction-app/
│
├── frontend/              → React App (Lovable/VS Code + Node.js)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
│
├── backend/               → Flask API (Python + VS Code)
│   ├── app.py
│   ├── requirements.txt
│   └── .gitignore
│
└── database/              → SQL (Already set up in Lovable Cloud)
    └── migrations/
```

---

## 🎨 FRONTEND SETUP

**Technology:** React + TypeScript + Vite  
**Tools Needed:** VS Code (or any code editor) + Node.js  
**Location:** This Lovable project (already running)

### Frontend Files:
- `src/components/StockSearch.tsx` - Stock search component
- `src/components/TrendChart.tsx` - Chart visualization  
- `src/components/Watchlist.tsx` - User watchlist
- `src/pages/Dashboard.tsx` - Main dashboard
- `src/pages/Chat.tsx` - AI chat interface
- `src/services/stockApi.ts` - Flask backend connection

### How to Run Frontend:
1. **In Lovable:** Already running (what you see now)
2. **Locally in VS Code:**
   ```bash
   npm install
   npm run dev
   ```

---

## 🐍 BACKEND SETUP

**Technology:** Flask + Python + Machine Learning  
**Tools Needed:** VS Code + Python 3.8+  
**Server:** Gunicorn (production) or Flask dev server (local)

### Backend Files in `backend/` folder:

1. **app.py** - Main Flask application
2. **requirements.txt** - Python dependencies
3. **.gitignore** - Git ignore file
4. **README.md** - Backend documentation

### How to Run Backend:

**Option 1: Local Development**
```bash
cd backend/
pip install -r requirements.txt
python app.py
```
Runs on: `http://localhost:5000`

**Option 2: Production (Heroku/Railway/Render)**
- Deploy using Git
- Uses Gunicorn server automatically

---

## 🗄️ DATABASE SETUP

**Technology:** PostgreSQL (Lovable Cloud/Supabase)  
**Tools Needed:** None (already configured)  
**Access:** Through Lovable dashboard

### Database Tables:
- `profiles` - User profiles
- `watchlist` - User stock watchlist
- `stock_data` - Historical stock prices
- `stock_predictions` - ML predictions
- `chat_messages` - Chat history

### Connection Details:
Already connected in both frontend and backend automatically!

---

## 🔗 HOW THEY CONNECT

```
Frontend (React)  →  Backend (Flask)  →  Database (PostgreSQL)
   Port: 3000          Port: 5000           Cloud
```

1. **Frontend** makes HTTP requests to Flask backend
2. **Backend** processes ML predictions and fetches Yahoo Finance data
3. **Backend** saves/retrieves data from database
4. **Frontend** displays results to user

---

## 🚀 DEPLOYMENT OPTIONS

### Frontend Deployment:
- **Lovable:** Click "Publish" button (easiest)
- **Vercel:** Connect GitHub repo
- **Netlify:** Connect GitHub repo

### Backend Deployment:
- **Heroku:** `git push heroku main`
- **Railway.app:** Connect GitHub repo
- **Render.com:** Connect GitHub repo
- **Google Cloud Run:** Docker deployment

---

## 🛠️ WHICH APP FOR WHAT?

| Component | Tool/App | Purpose |
|-----------|----------|---------|
| **Frontend Code** | VS Code / Lovable | Edit React components |
| **Backend Code** | VS Code / PyCharm | Edit Python Flask code |
| **Run Frontend** | Node.js (via npm) | Execute React app |
| **Run Backend** | Python 3.8+ | Execute Flask server |
| **Database** | Lovable Dashboard | View/manage data |
| **Deploy Frontend** | Lovable/Vercel | Host React app |
| **Deploy Backend** | Heroku/Railway | Host Flask API |

---

## 📝 QUICK START CHECKLIST

- [x] Database created (already done)
- [ ] Backend running locally (`python app.py`)
- [ ] Frontend connecting to backend
- [ ] Test stock search
- [ ] Test ML predictions
- [ ] Deploy backend to production
- [ ] Update frontend with production URL

---

## 🆘 NEED HELP?

- **Frontend issues:** Check browser console (F12)
- **Backend issues:** Check terminal logs
- **Database issues:** Check Lovable backend panel
- **Connection issues:** Verify CORS is enabled in Flask
