/**
 * FRONTEND COMPONENT
 * Location: frontend/src/components/StockSearch.tsx
 * Tool: VS Code + Node.js (React)
 */

import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Search, Plus } from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { supabase } from "@/integrations/supabase/client";
import { fetchStockData } from "@/services/stockApi";

interface StockSearchProps {
  onSelectStock: (symbol: string) => void;
}

export const StockSearch = ({ onSelectStock }: StockSearchProps) => {
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setLoading(true);
    try {
      // Fetch real stock data from Flask backend
      const stockData = await fetchStockData(searchQuery.toUpperCase());
      onSelectStock(searchQuery.toUpperCase());
      toast({
        title: "Stock Data Loaded",
        description: `Current price: $${stockData.current_price.toFixed(2)}`,
      });
    } catch (error: any) {
      toast({
        title: "Error",
        description: error.message || "Failed to fetch stock data",
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleAddToWatchlist = async () => {
    if (!searchQuery.trim()) {
      toast({
        title: "Error",
        description: "Please enter a stock symbol",
        variant: "destructive",
      });
      return;
    }

    try {
      const {
        data: { user },
      } = await supabase.auth.getUser();

      if (!user) {
        toast({
          title: "Error",
          description: "Please sign in to add to watchlist",
          variant: "destructive",
        });
        return;
      }

      const { error } = await supabase.from("watchlist").insert({
        user_id: user.id,
        symbol: searchQuery.toUpperCase(),
        company_name: searchQuery.toUpperCase(),
      });

      if (error) {
        if (error.code === "23505") {
          toast({
            title: "Already in watchlist",
            description: "This stock is already in your watchlist",
          });
        } else {
          throw error;
        }
      } else {
        toast({
          title: "Added to watchlist",
          description: `${searchQuery.toUpperCase()} has been added to your watchlist`,
        });
        setSearchQuery("");
      }
    } catch (error: any) {
      toast({
        title: "Error",
        description: error.message,
        variant: "destructive",
      });
    }
  };

  return (
    <form onSubmit={handleSearch} className="flex gap-2">
      <div className="flex-1 flex gap-2">
        <Input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Search stock symbol (e.g., AAPL, GOOGL)"
          className="bg-background/50"
        />
        <Button type="submit" disabled={loading} className="bg-gradient-primary">
          <Search className="h-4 w-4 mr-2" />
          Search
        </Button>
      </div>
      <Button
        type="button"
        variant="outline"
        onClick={handleAddToWatchlist}
        className="border-primary/50"
      >
        <Plus className="h-4 w-4 mr-2" />
        Add to Watchlist
      </Button>
    </form>
  );
};