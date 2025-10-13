/**
 * FRONTEND SERVICE FILE
 * Location: frontend/src/services/stockApi.ts
 * Tool: VS Code + Node.js
 * Purpose: Connect React frontend to Flask backend
 */

// Change this URL when deploying backend to production
const FLASK_API_URL = import.meta.env.VITE_FLASK_API_URL || 'http://localhost:5000';

export interface StockData {
  symbol: string;
  data: Array<{
    Date: string;
    Open: number;
    High: number;
    Low: number;
    Close: number;
    Volume: number;
  }>;
  current_price: number;
}

export interface PredictionData {
  symbol: string;
  predicted_price: number;
  current_price: number;
  model_type: string;
  confidence: number;
}

/**
 * Fetch stock data from Flask backend
 */
export const fetchStockData = async (symbol: string): Promise<StockData> => {
  try {
    const response = await fetch(`${FLASK_API_URL}/api/get_stock_data/${symbol}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching stock data:', error);
    throw error;
  }
};

/**
 * Get ML prediction from Flask backend
 */
export const getPrediction = async (
  symbol: string,
  userId: string,
  modelType: 'SVM' | 'DecisionTree' | 'RandomForest' | 'LSTM' = 'RandomForest'
): Promise<PredictionData> => {
  try {
    const response = await fetch(`${FLASK_API_URL}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        symbol,
        user_id: userId,
        model_type: modelType,
      }),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error getting prediction:', error);
    throw error;
  }
};

/**
 * Check if Flask backend is running
 */
export const checkBackendHealth = async (): Promise<boolean> => {
  try {
    const response = await fetch(`${FLASK_API_URL}/health`);
    return response.ok;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
};
