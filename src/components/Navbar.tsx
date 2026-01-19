import { Link, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Home, TrendingUp, MessageSquare, User, LogOut } from "lucide-react";
import { useAuth } from "@/contexts/AuthContext";
import { useToast } from "@/hooks/use-toast";
import logo from "@/assets/logo.png";

export const Navbar = () => {
  const navigate = useNavigate();
  const { toast } = useToast();
  const { user, logout, isAuthenticated } = useAuth();

  const handleSignOut = () => {
    logout();
    toast({
      title: "Signed out",
      description: "You've been successfully signed out.",
    });
    navigate("/auth");
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-lg border-b border-border">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center gap-3">
            <img src={logo} alt="StockAI" className="h-10" />
            <span className="text-xl font-bold bg-gradient-primary bg-clip-text text-transparent">
              StockAI
            </span>
          </Link>

          <div className="hidden md:flex items-center gap-6">
            <Link to="/" className="flex items-center gap-2 text-foreground hover:text-primary transition-colors">
              <Home className="h-4 w-4" />
              <span>Home</span>
            </Link>
            {isAuthenticated && (
              <>
                <Link to="/dashboard" className="flex items-center gap-2 text-foreground hover:text-primary transition-colors">
                  <TrendingUp className="h-4 w-4" />
                  <span>Dashboard</span>
                </Link>
                <Link to="/chat" className="flex items-center gap-2 text-foreground hover:text-primary transition-colors">
                  <MessageSquare className="h-4 w-4" />
                  <span>AI Assistant</span>
                </Link>
              </>
            )}
          </div>

          <div className="flex items-center gap-3">
            {isAuthenticated ? (
              <>
                <Button variant="ghost" size="icon" onClick={() => navigate("/profile")}>
                  <User className="h-5 w-5" />
                </Button>
                <Button variant="ghost" size="icon" onClick={handleSignOut}>
                  <LogOut className="h-5 w-5" />
                </Button>
              </>
            ) : (
              <Button onClick={() => navigate("/auth")} className="bg-gradient-primary">
                Get Started
              </Button>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};
