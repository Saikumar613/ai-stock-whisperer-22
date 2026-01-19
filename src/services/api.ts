/**
 * Flask Backend API Service
 * Handles all communication with the Flask backend
 */

// Change this URL when deploying backend to production
const API_URL = import.meta.env.VITE_FLASK_API_URL || 'http://localhost:5000';

// Token storage key
const TOKEN_KEY = 'stockai_token';
const USER_KEY = 'stockai_user';

// ============================================
// AUTH HELPERS
// ============================================

export const getToken = (): string | null => {
  return localStorage.getItem(TOKEN_KEY);
};

export const setToken = (token: string): void => {
  localStorage.setItem(TOKEN_KEY, token);
};

export const removeToken = (): void => {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
};

export const getStoredUser = (): User | null => {
  const user = localStorage.getItem(USER_KEY);
  return user ? JSON.parse(user) : null;
};

export const setStoredUser = (user: User): void => {
  localStorage.setItem(USER_KEY, JSON.stringify(user));
};

// ============================================
// TYPES
// ============================================

export interface User {
  id: string;
  email: string;
  full_name?: string;
  created_at?: string;
}

export interface AuthResponse {
  message: string;
  token: string;
  user: User;
}

export interface StockData {
  symbol: string;
  name?: string;
  sector?: string;
  current_price: number;
  previous_close?: number;
  market_cap?: number;
  pe_ratio?: number;
  data: Array<{
    Date: string;
    Open: number;
    High: number;
    Low: number;
    Close: number;
    Volume: number;
  }>;
}

export interface PredictionData {
  symbol: string;
  predicted_price: number;
  current_price: number;
  price_change_percent: number;
  confidence: number;
  model_type: string;
  recommendation: string;
  prediction_date: string;
}

export interface WatchlistItem {
  _id: string;
  id?: string;
  user_id: string;
  symbol: string;
  company_name: string;
  current_price?: number;
  added_at: string;
}

export interface ChatMessage {
  _id?: string;
  id?: string;
  user_id: string;
  content: string;
  role: 'user' | 'assistant';
  created_at: string;
}

// ============================================
// API HELPERS
// ============================================

const getAuthHeaders = (): Record<string, string> => {
  const token = getToken();
  return {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {})
  };
};

const handleResponse = async (response: Response) => {
  const data = await response.json();
  
  if (!response.ok) {
    throw new Error(data.error || `HTTP error! status: ${response.status}`);
  }
  
  return data;
};

// ============================================
// AUTH API
// ============================================

export const authApi = {
  signup: async (email: string, password: string, fullName: string): Promise<AuthResponse> => {
    const response = await fetch(`${API_URL}/api/auth/signup`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, full_name: fullName })
    });
    
    const data = await handleResponse(response);
    setToken(data.token);
    setStoredUser(data.user);
    return data;
  },

  login: async (email: string, password: string): Promise<AuthResponse> => {
    const response = await fetch(`${API_URL}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    
    const data = await handleResponse(response);
    setToken(data.token);
    setStoredUser(data.user);
    return data;
  },

  logout: (): void => {
    removeToken();
  },

  getMe: async (): Promise<{ user: User }> => {
    const response = await fetch(`${API_URL}/api/auth/me`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    const data = await handleResponse(response);
    setStoredUser(data.user);
    return data;
  },

  updatePassword: async (newPassword: string): Promise<{ message: string }> => {
    const response = await fetch(`${API_URL}/api/auth/update-password`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ password: newPassword })
    });
    
    return handleResponse(response);
  },

  isAuthenticated: (): boolean => {
    return !!getToken();
  }
};

// ============================================
// STOCK API
// ============================================

export const stockApi = {
  getStockData: async (symbol: string, period: string = '1y'): Promise<StockData> => {
    const response = await fetch(`${API_URL}/api/get_stock_data/${symbol}?period=${period}`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  },

  searchStocks: async (query: string): Promise<any[]> => {
    const response = await fetch(`${API_URL}/api/search/${query}`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  },

  getSymbols: async (sector?: string, search?: string): Promise<any[]> => {
    let url = `${API_URL}/api/symbols`;
    const params = new URLSearchParams();
    if (sector) params.append('sector', sector);
    if (search) params.append('search', search);
    if (params.toString()) url += `?${params.toString()}`;
    
    const response = await fetch(url, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  },

  getSectors: async (): Promise<Array<{ name: string; count: number }>> => {
    const response = await fetch(`${API_URL}/api/sectors`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  }
};

// ============================================
// PREDICTION API
// ============================================

export const predictionApi = {
  predict: async (
    symbol: string, 
    modelType: 'SVM' | 'DecisionTree' | 'RandomForest' | 'LSTM' = 'RandomForest'
  ): Promise<PredictionData> => {
    const response = await fetch(`${API_URL}/api/predict`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ symbol, model_type: modelType })
    });
    
    return handleResponse(response);
  },

  getHistory: async (): Promise<any[]> => {
    const response = await fetch(`${API_URL}/api/predictions`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  }
};

// ============================================
// WATCHLIST API
// ============================================

export const watchlistApi = {
  getWatchlist: async (): Promise<WatchlistItem[]> => {
    const response = await fetch(`${API_URL}/api/watchlist`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  },

  addToWatchlist: async (symbol: string, companyName: string): Promise<{ id: string; message: string }> => {
    const response = await fetch(`${API_URL}/api/watchlist`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ symbol, company_name: companyName })
    });
    
    return handleResponse(response);
  },

  removeFromWatchlist: async (itemId: string): Promise<{ message: string }> => {
    const response = await fetch(`${API_URL}/api/watchlist/${itemId}`, {
      method: 'DELETE',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  }
};

// ============================================
// CHAT API
// ============================================

export const chatApi = {
  getHistory: async (): Promise<ChatMessage[]> => {
    const response = await fetch(`${API_URL}/api/chat/history`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    
    return handleResponse(response);
  },

  sendMessage: async (message: string): Promise<{ response: string }> => {
    const response = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ message })
    });
    
    return handleResponse(response);
  }
};

// ============================================
// HEALTH CHECK
// ============================================

export const checkBackendHealth = async (): Promise<boolean> => {
  try {
    const response = await fetch(`${API_URL}/health`);
    return response.ok;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
};

// Default exports for backward compatibility
export const fetchStockData = stockApi.getStockData;
export const getPrediction = predictionApi.predict;
