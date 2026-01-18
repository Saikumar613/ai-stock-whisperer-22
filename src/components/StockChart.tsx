import { useEffect, useState } from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { TrendingUp, TrendingDown, Loader2, RefreshCw } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface StockChartProps {
  symbol: string;
  onPredictionRequest?: (symbol: string, modelType: string) => void;
  apiUrl?: string;
}

interface ChartDataPoint {
  date: string;
  price: number;
  volume?: number;
}

interface StockInfo {
  symbol: string;
  name: string;
  current_price: number;
  change: number;
  change_percent: number;
}

export const StockChart = ({ 
  symbol, 
  onPredictionRequest,
  apiUrl = "http://localhost:5000" 
}: StockChartProps) => {
  const [chartData, setChartData] = useState<ChartDataPoint[]>([]);
  const [stockInfo, setStockInfo] = useState<StockInfo | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [timeRange, setTimeRange] = useState<string>("1M");
  const [modelType, setModelType] = useState<string>("RandomForest");

  const fetchStockData = async () => {
    if (!symbol) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(`${apiUrl}/api/get_stock_data/${symbol}`);
      
      if (!response.ok) {
        throw new Error(`Failed to fetch data for ${symbol}`);
      }
      
      const result = await response.json();
      
      // Transform data for chart
      const dataPoints = getDataForTimeRange(result.data, timeRange);
      const formattedData = dataPoints.map((item: any) => ({
        date: new Date(item.Date).toLocaleDateString("en-US", { 
          month: "short", 
          day: "numeric" 
        }),
        price: parseFloat(item.Close.toFixed(2)),
        volume: item.Volume,
      }));
      
      setChartData(formattedData);
      
      // Set stock info
      if (result.data && result.data.length > 0) {
        const latestData = result.data[result.data.length - 1];
        const previousData = result.data[result.data.length - 2];
        const change = latestData.Close - previousData.Close;
        const changePercent = (change / previousData.Close) * 100;
        
        setStockInfo({
          symbol: symbol,
          name: result.company_name || symbol,
          current_price: latestData.Close,
          change: change,
          change_percent: changePercent,
        });
      }
    } catch (err: any) {
      setError(err.message || "Failed to load stock data");
    } finally {
      setLoading(false);
    }
  };

  const getDataForTimeRange = (data: any[], range: string) => {
    if (!data || data.length === 0) return [];
    
    const rangeMap: { [key: string]: number } = {
      "1W": 7,
      "1M": 30,
      "3M": 90,
      "6M": 180,
      "1Y": 365,
    };
    
    const days = rangeMap[range] || 30;
    return data.slice(-days);
  };

  useEffect(() => {
    fetchStockData();
  }, [symbol, timeRange]);

  const handlePredict = () => {
    if (onPredictionRequest) {
      onPredictionRequest(symbol, modelType);
    }
  };

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-card/95 backdrop-blur-sm border border-border p-3 rounded-lg shadow-lg">
          <p className="text-sm font-medium text-foreground">{payload[0].payload.date}</p>
          <p className="text-sm text-primary font-semibold">
            ${payload[0].value.toFixed(2)}
          </p>
        </div>
      );
    }
    return null;
  };

  if (loading) {
    return (
      <Card className="w-full">
        <CardContent className="flex items-center justify-center h-80">
          <Loader2 className="h-8 w-8 animate-spin text-primary" />
        </CardContent>
      </Card>
    );
  }

  if (error) {
    return (
      <Card className="w-full">
        <CardContent className="flex flex-col items-center justify-center h-80 gap-4">
          <p className="text-destructive">{error}</p>
          <Button onClick={fetchStockData} variant="outline">
            <RefreshCw className="h-4 w-4 mr-2" />
            Retry
          </Button>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="w-full">
      <CardHeader className="pb-2">
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div className="flex items-center gap-4">
            <CardTitle className="text-xl">{symbol}</CardTitle>
            {stockInfo && (
              <div className="flex items-center gap-2">
                <span className="text-2xl font-bold">
                  ${stockInfo.current_price.toFixed(2)}
                </span>
                <div className={`flex items-center gap-1 ${
                  stockInfo.change >= 0 ? "text-green-500" : "text-red-500"
                }`}>
                  {stockInfo.change >= 0 ? (
                    <TrendingUp className="h-4 w-4" />
                  ) : (
                    <TrendingDown className="h-4 w-4" />
                  )}
                  <span className="text-sm font-medium">
                    {stockInfo.change >= 0 ? "+" : ""}
                    {stockInfo.change.toFixed(2)} ({stockInfo.change_percent.toFixed(2)}%)
                  </span>
                </div>
              </div>
            )}
          </div>
          
          <div className="flex items-center gap-2">
            <Select value={timeRange} onValueChange={setTimeRange}>
              <SelectTrigger className="w-20">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="1W">1W</SelectItem>
                <SelectItem value="1M">1M</SelectItem>
                <SelectItem value="3M">3M</SelectItem>
                <SelectItem value="6M">6M</SelectItem>
                <SelectItem value="1Y">1Y</SelectItem>
              </SelectContent>
            </Select>
            
            <Button onClick={fetchStockData} variant="ghost" size="icon">
              <RefreshCw className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </CardHeader>
      
      <CardContent>
        {/* Prediction Controls */}
        {onPredictionRequest && (
          <div className="flex items-center gap-2 mb-4 p-3 bg-muted/50 rounded-lg">
            <Select value={modelType} onValueChange={setModelType}>
              <SelectTrigger className="w-40">
                <SelectValue placeholder="ML Model" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="RandomForest">Random Forest</SelectItem>
                <SelectItem value="SVM">SVM</SelectItem>
                <SelectItem value="DecisionTree">Decision Tree</SelectItem>
                <SelectItem value="LSTM">LSTM</SelectItem>
              </SelectContent>
            </Select>
            
            <Button onClick={handlePredict} className="bg-primary">
              Run Prediction
            </Button>
          </div>
        )}
        
        {/* Chart */}
        <div className="h-64">
          {chartData.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={chartData}>
                <defs>
                  <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="hsl(var(--primary))" stopOpacity={0.3} />
                    <stop offset="95%" stopColor="hsl(var(--primary))" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid 
                  strokeDasharray="3 3" 
                  stroke="hsl(var(--border))" 
                  opacity={0.3} 
                />
                <XAxis
                  dataKey="date"
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  tickLine={false}
                />
                <YAxis
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  tickLine={false}
                  domain={["auto", "auto"]}
                  tickFormatter={(value) => `$${value}`}
                />
                <Tooltip content={<CustomTooltip />} />
                <Area
                  type="monotone"
                  dataKey="price"
                  stroke="hsl(var(--primary))"
                  strokeWidth={2}
                  fill="url(#colorPrice)"
                />
              </AreaChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex items-center justify-center h-full text-muted-foreground">
              No data available
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};
