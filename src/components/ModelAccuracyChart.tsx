import { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from "recharts";
import { Loader2, BarChart3 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { useToast } from "@/hooks/use-toast";
import { useAuth } from "@/contexts/AuthContext";
import { getToken } from "@/services/api";

const API_URL = import.meta.env.VITE_FLASK_API_URL || "http://localhost:5000";

const MODEL_COLORS = [
  "hsl(var(--chart-primary))",
  "hsl(var(--accent))",
  "hsl(var(--destructive))",
  "hsl(199, 70%, 65%)",
];

interface ModelResult {
  model: string;
  accuracy: number;
  mae: number;
  rmse: number;
  r2_score: number;
  mae_price: number;
  error?: string;
}

interface CompareResponse {
  symbol: string;
  models: ModelResult[];
  data_points: number;
  test_size: number;
}

interface ModelAccuracyChartProps {
  selectedStock: string | null;
}

export const ModelAccuracyChart = ({ selectedStock }: ModelAccuracyChartProps) => {
  const [data, setData] = useState<CompareResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();
  const { isAuthenticated } = useAuth();

  const handleCompare = async () => {
    if (!selectedStock) return;
    if (!isAuthenticated) {
      toast({ title: "Sign in required", description: "Please sign in to compare models", variant: "destructive" });
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`${API_URL}/api/compare_models`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${getToken()}`,
        },
        body: JSON.stringify({ symbol: selectedStock }),
      });
      const json = await res.json();
      if (!res.ok) throw new Error(json.error || "Failed to compare models");
      setData(json);
      toast({ title: "Comparison complete", description: `Analyzed ${json.data_points} data points across 4 models` });
    } catch (err: any) {
      toast({ title: "Comparison failed", description: err.message, variant: "destructive" });
    } finally {
      setLoading(false);
    }
  };

  const CustomBarTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      const d = payload[0].payload as ModelResult;
      return (
        <div className="bg-card/95 backdrop-blur-sm border border-border p-3 rounded-lg shadow-lg text-sm space-y-1">
          <p className="font-semibold text-primary">{d.model}</p>
          <p>Accuracy (R²): <span className="font-mono font-bold">{d.accuracy}%</span></p>
          <p>MAE (price): <span className="font-mono">${d.mae_price}</span></p>
          <p>RMSE: <span className="font-mono">{d.rmse}</span></p>
          {d.error && <p className="text-destructive text-xs">{d.error}</p>}
        </div>
      );
    }
    return null;
  };

  if (!selectedStock) {
    return (
      <div className="flex flex-col items-center justify-center h-64 text-muted-foreground gap-2">
        <BarChart3 className="h-12 w-12 opacity-20" />
        <p className="text-center text-sm">Select a stock to compare ML model accuracies</p>
      </div>
    );
  }

  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-4">
        <div>
          <p className="text-sm text-muted-foreground">Comparing models for</p>
          <p className="text-lg font-semibold text-primary">{selectedStock}</p>
        </div>
        <Button onClick={handleCompare} disabled={loading} className="bg-gradient-primary">
          {loading && <Loader2 className="h-4 w-4 mr-2 animate-spin" />}
          {loading ? "Analyzing..." : "Compare All Models"}
        </Button>
      </div>

      {loading && (
        <div className="flex items-center justify-center h-64">
          <div className="text-center space-y-3">
            <Loader2 className="h-8 w-8 animate-spin text-primary mx-auto" />
            <p className="text-sm text-muted-foreground">Training SVM, Decision Tree, Random Forest & LSTM...</p>
          </div>
        </div>
      )}

      {!loading && data && (
        <Tabs defaultValue="accuracy" className="w-full">
          <TabsList className="mb-4">
            <TabsTrigger value="accuracy">Accuracy</TabsTrigger>
            <TabsTrigger value="error">Price Error</TabsTrigger>
            <TabsTrigger value="radar">Radar</TabsTrigger>
          </TabsList>

          <TabsContent value="accuracy">
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={data.models} layout="vertical" margin={{ left: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
                  <XAxis type="number" domain={[0, 100]} stroke="hsl(var(--muted-foreground))" fontSize={12} unit="%" />
                  <YAxis dataKey="model" type="category" stroke="hsl(var(--muted-foreground))" fontSize={13} width={110} />
                  <Tooltip content={<CustomBarTooltip />} />
                  <Bar dataKey="accuracy" radius={[0, 6, 6, 0]} barSize={28}>
                    {data.models.map((_, i) => (
                      <Cell key={i} fill={MODEL_COLORS[i % MODEL_COLORS.length]} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
            <p className="text-xs text-muted-foreground mt-2 text-center">
              R² score as percentage · {data.test_size} test samples from {data.data_points} total data points
            </p>
          </TabsContent>

          <TabsContent value="error">
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={data.models} layout="vertical" margin={{ left: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
                  <XAxis type="number" stroke="hsl(var(--muted-foreground))" fontSize={12} unit="$" />
                  <YAxis dataKey="model" type="category" stroke="hsl(var(--muted-foreground))" fontSize={13} width={110} />
                  <Tooltip content={({ active, payload }: any) => {
                    if (active && payload?.[0]) {
                      const d = payload[0].payload as ModelResult;
                      return (
                        <div className="bg-card/95 backdrop-blur-sm border border-border p-3 rounded-lg shadow-lg text-sm">
                          <p className="font-semibold text-primary">{d.model}</p>
                          <p>Avg Price Error: <span className="font-mono font-bold">${d.mae_price}</span></p>
                        </div>
                      );
                    }
                    return null;
                  }} />
                  <Bar dataKey="mae_price" radius={[0, 6, 6, 0]} barSize={28}>
                    {data.models.map((_, i) => (
                      <Cell key={i} fill={MODEL_COLORS[i % MODEL_COLORS.length]} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
            <p className="text-xs text-muted-foreground mt-2 text-center">
              Mean Absolute Error in dollars · Lower is better
            </p>
          </TabsContent>

          <TabsContent value="radar">
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={data.models.map(m => ({
                  model: m.model,
                  Accuracy: m.accuracy,
                  Precision: Math.max(0, 100 - m.rmse * 100),
                  Reliability: Math.max(0, 100 - m.mae * 100),
                }))}>
                  <PolarGrid stroke="hsl(var(--border))" />
                  <PolarAngleAxis dataKey="model" stroke="hsl(var(--muted-foreground))" fontSize={12} />
                  <PolarRadiusAxis domain={[0, 100]} stroke="hsl(var(--muted-foreground))" fontSize={10} />
                  <Radar name="Accuracy" dataKey="Accuracy" stroke="hsl(var(--chart-primary))" fill="hsl(var(--chart-primary))" fillOpacity={0.3} />
                  <Radar name="Precision" dataKey="Precision" stroke="hsl(var(--accent))" fill="hsl(var(--accent))" fillOpacity={0.2} />
                  <Radar name="Reliability" dataKey="Reliability" stroke="hsl(var(--destructive))" fill="hsl(var(--destructive))" fillOpacity={0.15} />
                </RadarChart>
              </ResponsiveContainer>
            </div>
            <p className="text-xs text-muted-foreground mt-2 text-center">
              Multi-metric radar comparison across all models
            </p>
          </TabsContent>
        </Tabs>
      )}
    </div>
  );
};
