import { TrendingUp, TrendingDown, Brain, Calendar, Target, Percent } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface PredictionData {
  symbol: string;
  predicted_price: number;
  current_price: number;
  confidence: number;
  model_type: string;
  prediction_date: string;
  direction?: "up" | "down";
}

interface PredictionCardProps {
  prediction: PredictionData;
  showDetails?: boolean;
}

export const PredictionCard = ({ prediction, showDetails = true }: PredictionCardProps) => {
  const priceChange = prediction.predicted_price - prediction.current_price;
  const percentChange = (priceChange / prediction.current_price) * 100;
  const isPositive = priceChange >= 0;

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 80) return "text-green-500 bg-green-500/10";
    if (confidence >= 60) return "text-yellow-500 bg-yellow-500/10";
    return "text-red-500 bg-red-500/10";
  };

  const getModelBadgeColor = (model: string) => {
    const colors: { [key: string]: string } = {
      RandomForest: "bg-emerald-500/10 text-emerald-500 border-emerald-500/20",
      SVM: "bg-blue-500/10 text-blue-500 border-blue-500/20",
      DecisionTree: "bg-purple-500/10 text-purple-500 border-purple-500/20",
      LSTM: "bg-orange-500/10 text-orange-500 border-orange-500/20",
    };
    return colors[model] || "bg-muted text-muted-foreground";
  };

  return (
    <Card className="w-full overflow-hidden">
      <CardHeader className="pb-2">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Brain className="h-5 w-5 text-primary" />
            <CardTitle className="text-lg">{prediction.symbol}</CardTitle>
          </div>
          <Badge 
            variant="outline" 
            className={getModelBadgeColor(prediction.model_type)}
          >
            {prediction.model_type}
          </Badge>
        </div>
      </CardHeader>
      
      <CardContent className="space-y-4">
        {/* Main Prediction Display */}
        <div className="flex items-center justify-between p-4 rounded-lg bg-muted/50">
          <div>
            <p className="text-sm text-muted-foreground mb-1">Predicted Price</p>
            <p className="text-3xl font-bold text-foreground">
              ${prediction.predicted_price.toFixed(2)}
            </p>
          </div>
          
          <div className={`flex items-center gap-2 px-3 py-2 rounded-lg ${
            isPositive ? "bg-green-500/10" : "bg-red-500/10"
          }`}>
            {isPositive ? (
              <TrendingUp className="h-6 w-6 text-green-500" />
            ) : (
              <TrendingDown className="h-6 w-6 text-red-500" />
            )}
            <div className={isPositive ? "text-green-500" : "text-red-500"}>
              <p className="text-lg font-bold">
                {isPositive ? "+" : ""}{percentChange.toFixed(2)}%
              </p>
              <p className="text-xs">
                {isPositive ? "+" : ""}${priceChange.toFixed(2)}
              </p>
            </div>
          </div>
        </div>

        {/* Details Grid */}
        {showDetails && (
          <div className="grid grid-cols-2 gap-3">
            <div className="flex items-center gap-2 p-3 rounded-lg bg-muted/30">
              <Target className="h-4 w-4 text-muted-foreground" />
              <div>
                <p className="text-xs text-muted-foreground">Current Price</p>
                <p className="text-sm font-semibold">${prediction.current_price.toFixed(2)}</p>
              </div>
            </div>
            
            <div className={`flex items-center gap-2 p-3 rounded-lg ${getConfidenceColor(prediction.confidence)}`}>
              <Percent className="h-4 w-4" />
              <div>
                <p className="text-xs opacity-80">Confidence</p>
                <p className="text-sm font-semibold">{prediction.confidence.toFixed(1)}%</p>
              </div>
            </div>
            
            <div className="flex items-center gap-2 p-3 rounded-lg bg-muted/30 col-span-2">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <div>
                <p className="text-xs text-muted-foreground">Prediction Date</p>
                <p className="text-sm font-semibold">
                  {new Date(prediction.prediction_date).toLocaleDateString("en-US", {
                    weekday: "short",
                    month: "short",
                    day: "numeric",
                    year: "numeric",
                  })}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Disclaimer */}
        <p className="text-xs text-muted-foreground text-center pt-2 border-t border-border">
          AI predictions are for informational purposes only. Not financial advice.
        </p>
      </CardContent>
    </Card>
  );
};

// Compact version for lists
export const PredictionCardCompact = ({ prediction }: { prediction: PredictionData }) => {
  const priceChange = prediction.predicted_price - prediction.current_price;
  const percentChange = (priceChange / prediction.current_price) * 100;
  const isPositive = priceChange >= 0;

  return (
    <div className="flex items-center justify-between p-3 rounded-lg border bg-card hover:bg-muted/50 transition-colors">
      <div className="flex items-center gap-3">
        <div className={`p-2 rounded-full ${isPositive ? "bg-green-500/10" : "bg-red-500/10"}`}>
          {isPositive ? (
            <TrendingUp className="h-4 w-4 text-green-500" />
          ) : (
            <TrendingDown className="h-4 w-4 text-red-500" />
          )}
        </div>
        <div>
          <p className="font-semibold">{prediction.symbol}</p>
          <p className="text-xs text-muted-foreground">{prediction.model_type}</p>
        </div>
      </div>
      
      <div className="text-right">
        <p className="font-semibold">${prediction.predicted_price.toFixed(2)}</p>
        <p className={`text-xs ${isPositive ? "text-green-500" : "text-red-500"}`}>
          {isPositive ? "+" : ""}{percentChange.toFixed(2)}%
        </p>
      </div>
    </div>
  );
};
