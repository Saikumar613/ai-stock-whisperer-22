import { useEffect, useState } from "react";
import { supabase } from "@/integrations/supabase/client";
import { Button } from "@/components/ui/button";
import { Trash2, TrendingUp, TrendingDown } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

interface WatchlistProps {
  userId: string;
  onSelectStock: (symbol: string) => void;
}

interface WatchlistItem {
  id: string;
  symbol: string;
  company_name: string;
}

export const Watchlist = ({ userId, onSelectStock }: WatchlistProps) => {
  const [items, setItems] = useState<WatchlistItem[]>([]);
  const [loading, setLoading] = useState(true);
  const { toast } = useToast();

  useEffect(() => {
    fetchWatchlist();
  }, [userId]);

  const fetchWatchlist = async () => {
    try {
      const { data, error } = await supabase
        .from("watchlist")
        .select("*")
        .eq("user_id", userId)
        .order("added_at", { ascending: false });

      if (error) throw error;
      setItems(data || []);
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
      const { error } = await supabase.from("watchlist").delete().eq("id", id);

      if (error) throw error;

      setItems(items.filter((item) => item.id !== id));
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

  // Generate random price changes for demo
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
            key={item.id}
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
                  handleRemove(item.id);
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