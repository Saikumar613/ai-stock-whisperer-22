import { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from "recharts";
import { TrendingUp, Loader2 } from "lucide-react";
import { stockApi, predictionApi } from "@/services/api";
import { useAuth } from "@/contexts/AuthContext";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface TrendChartProps {
  selectedStock: string | null;
}

export const TrendChart = ({ selectedStock }: TrendChartProps) => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [predicting, setPredicting] = useState(false);
  const [modelType, setModelType] = useState<'SVM' | 'DecisionTree' | 'RandomForest' | 'LSTM'>('RandomForest');
  const [prediction, setPrediction] = useState<number | null>(null);
  const { toast } = useToast();
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    if (!selectedStock) return;

    const loadStockData = async () => {
      setLoading(true);
      setPrediction(null);
      try {
        const stockData = await stockApi.getStockData(selectedStock);
        
        const chartData = stockData.data.slice(-30).map((item: any) => ({
          date: new Date(item.Date).toLocaleDateString("en-US", { month: "short", day: "numeric" }),
          price: parseFloat(item.Close.toFixed(2)),
        }));
        
        setData(chartData);
      } catch (error: any) {
        toast({
          title: "Error loading stock data",
          description: error.message,
          variant: "destructive",
        });
      } finally {
        setLoading(false);
      }
    };

    loadStockData();
  }, [selectedStock]);

  const handlePredict = async () => {
    if (!selectedStock) return;

    if (!isAuthenticated) {
      toast({
        title: "Authentication required",
        description: "Please sign in to use predictions",
        variant: "destructive",
      });
      return;
    }

    setPredicting(true);
    try {
      const predictionData = await predictionApi.predict(selectedStock, modelType);
      setPrediction(predictionData.predicted_price);
      
      toast({
        title: "Prediction Complete",
        description: `${modelType} predicts $${predictionData.predicted_price.toFixed(2)} (${predictionData.confidence.toFixed(1)}% confidence)`,
      });
    } catch (error: any) {
      toast({
        title: "Prediction failed",
        description: error.message,
        variant: "destructive",
      });
    } finally {
      setPredicting(false);
    }
  };

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-card/95 backdrop-blur-sm border border-border p-3 rounded-lg shadow-lg">
          <p className="text-sm font-medium mb-1">{payload[0].payload.date}</p>
          <p className="text-sm text-primary">
            Actual: ${payload[0].value}
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="w-full">
      {selectedStock && (
        <div className="mb-4 p-4 bg-primary/10 rounded-lg border border-primary/20">
          <div className="flex items-center justify-between mb-3">
            <div>
              <p className="text-sm text-muted-foreground">Currently analyzing</p>
              <p className="text-lg font-semibold text-primary">{selectedStock}</p>
            </div>
            {prediction && (
              <div className="text-right">
                <p className="text-sm text-muted-foreground">AI Prediction</p>
                <p className="text-xl font-bold text-accent">${prediction.toFixed(2)}</p>
              </div>
            )}
          </div>
          
          <div className="flex gap-2">
            <Select value={modelType} onValueChange={(value: any) => setModelType(value)}>
              <SelectTrigger className="w-40">
                <SelectValue placeholder="Model" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="RandomForest">Random Forest</SelectItem>
                <SelectItem value="SVM">SVM</SelectItem>
                <SelectItem value="DecisionTree">Decision Tree</SelectItem>
                <SelectItem value="LSTM">LSTM</SelectItem>
              </SelectContent>
            </Select>
            
            <Button 
              onClick={handlePredict} 
              disabled={predicting || loading}
              className="bg-gradient-primary"
            >
              {predicting && <Loader2 className="h-4 w-4 mr-2 animate-spin" />}
              {predicting ? 'Predicting...' : 'Run ML Prediction'}
            </Button>
          </div>
        </div>
      )}
      
      <div className="h-80">
        {loading ? (
          <div className="flex items-center justify-center h-full">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
          </div>
        ) : data.length > 0 && selectedStock ? (
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="hsl(var(--chart-primary))" stopOpacity={0.3} />
                <stop offset="95%" stopColor="hsl(var(--chart-primary))" stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
            <XAxis
              dataKey="date"
              stroke="hsl(var(--muted-foreground))"
              fontSize={12}
            />
            <YAxis
              stroke="hsl(var(--muted-foreground))"
              fontSize={12}
              domain={["auto", "auto"]}
            />
            <Tooltip content={<CustomTooltip />} />
            <Area
              type="monotone"
              dataKey="price"
              stroke="hsl(var(--chart-primary))"
              strokeWidth={2}
              fill="url(#colorPrice)"
              name="Actual Price"
            />
          </AreaChart>
          </ResponsiveContainer>
        ) : (
          <div className="flex flex-col items-center justify-center h-full text-muted-foreground gap-2">
            <TrendingUp className="h-12 w-12 opacity-20" />
            <p className="text-center">Search for a stock above to view AI-powered trends and predictions</p>
          </div>
        )}
      </div>
    </div>
  );
};
