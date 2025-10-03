import { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from "recharts";

interface TrendChartProps {
  selectedStock: string | null;
}

export const TrendChart = ({ selectedStock }: TrendChartProps) => {
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    // Generate sample data - in real app, this would fetch from API
    const generateData = () => {
      const days = 30;
      const basePrice = 100 + Math.random() * 100;
      const newData = [];

      for (let i = 0; i < days; i++) {
        const date = new Date();
        date.setDate(date.getDate() - (days - i));
        const variance = (Math.random() - 0.5) * 10;
        const price = basePrice + variance + (i * 0.5);

        newData.push({
          date: date.toLocaleDateString("en-US", { month: "short", day: "numeric" }),
          price: parseFloat(price.toFixed(2)),
          prediction: parseFloat((price + (Math.random() - 0.4) * 5).toFixed(2)),
        });
      }

      return newData;
    };

    setData(generateData());
  }, [selectedStock]);

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-card/95 backdrop-blur-sm border border-border p-3 rounded-lg shadow-lg">
          <p className="text-sm font-medium mb-1">{payload[0].payload.date}</p>
          <p className="text-sm text-primary">
            Actual: ${payload[0].value}
          </p>
          {payload[1] && (
            <p className="text-sm text-accent">
              Prediction: ${payload[1].value}
            </p>
          )}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="w-full h-80">
      {data.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="hsl(var(--chart-primary))" stopOpacity={0.3} />
                <stop offset="95%" stopColor="hsl(var(--chart-primary))" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="colorPrediction" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="hsl(var(--chart-secondary))" stopOpacity={0.3} />
                <stop offset="95%" stopColor="hsl(var(--chart-secondary))" stopOpacity={0} />
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
            <Area
              type="monotone"
              dataKey="prediction"
              stroke="hsl(var(--chart-secondary))"
              strokeWidth={2}
              strokeDasharray="5 5"
              fill="url(#colorPrediction)"
              name="AI Prediction"
            />
          </AreaChart>
        </ResponsiveContainer>
      ) : (
        <div className="flex items-center justify-center h-full text-muted-foreground">
          Search for a stock to view trends and predictions
        </div>
      )}
    </div>
  );
};