import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { Navbar } from "@/components/Navbar";
import { StockSearch } from "@/components/StockSearch";
import { TrendChart } from "@/components/TrendChart";
import { Watchlist } from "@/components/Watchlist";
import { Card } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

export default function Dashboard() {
  const { user, isAuthenticated, loading } = useAuth();
  const [selectedStock, setSelectedStock] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!loading && !isAuthenticated) {
      navigate("/auth");
    }
  }, [isAuthenticated, loading, navigate]);

  if (loading) {
    return (
      <div className="min-h-screen bg-background">
        <Navbar />
        <div className="container mx-auto px-4 pt-24">
          <Skeleton className="h-12 w-64 mb-8" />
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <Skeleton className="h-96 lg:col-span-2" />
            <Skeleton className="h-96" />
          </div>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) return null;

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      <div className="container mx-auto px-4 pt-24 pb-12">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">
            Welcome, <span className="bg-gradient-primary bg-clip-text text-transparent">{user?.email?.split('@')[0]}</span>
          </h1>
          <p className="text-muted-foreground">Track your favorite stocks and get AI-powered predictions</p>
        </div>

        <div className="mb-8">
          <StockSearch onSelectStock={setSelectedStock} />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <Card className="lg:col-span-2 p-6 bg-card/50 backdrop-blur-sm border-border">
            <h2 className="text-2xl font-semibold mb-4">Market Trends</h2>
            <TrendChart selectedStock={selectedStock} />
          </Card>

          <Card className="p-6 bg-card/50 backdrop-blur-sm border-border">
            <h2 className="text-2xl font-semibold mb-4">Your Watchlist</h2>
            <Watchlist onSelectStock={setSelectedStock} />
          </Card>
        </div>
      </div>
    </div>
  );
}
