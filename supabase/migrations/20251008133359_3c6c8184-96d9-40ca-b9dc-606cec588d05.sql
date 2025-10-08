-- Create table for storing stock predictions from ML models
CREATE TABLE public.stock_predictions (
  id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID NOT NULL,
  symbol TEXT NOT NULL,
  prediction_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  predicted_price DECIMAL(10, 2) NOT NULL,
  actual_price DECIMAL(10, 2),
  model_type TEXT NOT NULL, -- 'SVM', 'DecisionTree', 'RandomForest', 'LSTM'
  confidence DECIMAL(5, 2), -- confidence score (0-100)
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- Create table for storing historical stock data from Yahoo Finance
CREATE TABLE public.stock_data (
  id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  symbol TEXT NOT NULL,
  date TIMESTAMP WITH TIME ZONE NOT NULL,
  open_price DECIMAL(10, 2) NOT NULL,
  high_price DECIMAL(10, 2) NOT NULL,
  low_price DECIMAL(10, 2) NOT NULL,
  close_price DECIMAL(10, 2) NOT NULL,
  volume BIGINT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  UNIQUE(symbol, date)
);

-- Create index for faster lookups
CREATE INDEX idx_stock_data_symbol_date ON public.stock_data(symbol, date DESC);
CREATE INDEX idx_stock_predictions_user_symbol ON public.stock_predictions(user_id, symbol, prediction_date DESC);

-- Enable Row Level Security
ALTER TABLE public.stock_predictions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.stock_data ENABLE ROW LEVEL SECURITY;

-- RLS Policies for stock_predictions
CREATE POLICY "Users can view their own predictions"
  ON public.stock_predictions
  FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own predictions"
  ON public.stock_predictions
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- RLS Policies for stock_data (public read access for all authenticated users)
CREATE POLICY "Authenticated users can view stock data"
  ON public.stock_data
  FOR SELECT
  USING (auth.role() = 'authenticated');

CREATE POLICY "Service role can insert stock data"
  ON public.stock_data
  FOR INSERT
  WITH CHECK (true);