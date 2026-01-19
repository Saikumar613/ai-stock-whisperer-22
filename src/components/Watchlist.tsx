import { useEffect, useState } from "react";
import { watchlistApi, WatchlistItem } from "@/services/api";
import { Button } from "@/components/ui/button";
import { Trash2, TrendingUp, TrendingDown } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

interface WatchlistProps {
  onSelectStock: (symbol: string) => void;
}

export const Watchlist = ({ onSelectStock }: WatchlistProps) => {
  const [items, setItems] = useState<WatchlistItem[]>([]);
  const [loading, setLoading] = useState(true);
  const { toast } = useToast();

  useEffect(() => {
    fetchWatchlist();
  }, []);

  const fetchWatchlist = async () => {
    try {
      const data = await watchlistApi.getWatchlist();
      setItems(data);
    } catch (error: any) {
      toast({
        title: "Error",
        description: error.message,
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleRemove = async (id: string) => {
    try {
      await watchlistApi.removeFromWatchlist(id);
      setItems(items.filter((item) => item._id !== id));
      toast({
        title: "Removed",
        description: "Stock removed from watchlist",
      });
    } catch (error: any) {
      toast({
        title: "Error",
        description: error.message,
        variant: "destructive",
      });
    }
  };

  const getPriceChange = () => {
    const change = (Math.random() - 0.5) * 10;
    return {
      value: change.toFixed(2),
      positive: change > 0,
    };
  };

  if (loading) {
    return <div className="text-muted-foreground">Loading watchlist...</div>;
  }

  if (items.length === 0) {
    return (
      <div className="text-center text-muted-foreground py-8">
        <p>Your watchlist is empty</p>
        <p className="text-sm mt-2">Add stocks to track them here</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {items.map((item) => {
        const priceChange = getPriceChange();
        return (
          <div
            key={item._id}
            className="bg-background/50 p-4 rounded-lg border border-border hover:border-primary/50 transition-all cursor-pointer"
            onClick={() => onSelectStock(item.symbol)}
          >
            <div className="flex items-start justify-between mb-2">
              <div>
                <h3 className="font-semibold text-lg">{item.symbol}</h3>
                <p className="text-sm text-muted-foreground">{item.company_name}</p>
              </div>
              <Button
                size="icon"
                variant="ghost"
                onClick={(e) => {
                  e.stopPropagation();
                  handleRemove(item._id);
                }}
                className="h-8 w-8"
              >
                <Trash2 className="h-4 w-4 text-destructive" />
              </Button>
            </div>
            <div className="flex items-center gap-2">
              {priceChange.positive ? (
                <TrendingUp className="h-4 w-4 text-profit" />
              ) : (
                <TrendingDown className="h-4 w-4 text-loss" />
              )}
              <span
                className={`text-sm font-medium ${
                  priceChange.positive ? "text-profit" : "text-loss"
                }`}
              >
                {priceChange.positive ? "+" : ""}
                {priceChange.value}%
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
};
