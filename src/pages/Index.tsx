import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "@/integrations/supabase/client";
import { Button } from "@/components/ui/button";
import { Navbar } from "@/components/Navbar";
import { TrendingUp, Bot, BarChart3, Shield, Zap, Target } from "lucide-react";
import heroBg from "@/assets/hero-bg.jpg";

export default function Index() {
  const [user, setUser] = useState<any>(null);
  const navigate = useNavigate();

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null);
    });

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null);
    });

    return () => subscription.unsubscribe();
  }, []);

  const features = [
    {
      icon: Bot,
      title: "AI-Powered Predictions",
      description: "Advanced LSTM models analyze historical data for accurate stock forecasts",
    },
    {
      icon: TrendingUp,
      title: "Real-Time Analytics",
      description: "Track market trends and daily fluctuations with live data updates",
    },
    {
      icon: BarChart3,
      title: "Smart Visualizations",
      description: "Interactive charts and graphs make complex data easy to understand",
    },
    {
      icon: Shield,
      title: "Risk Assessment",
      description: "Get personalized risk analysis to make informed investment decisions",
    },
    {
      icon: Zap,
      title: "Instant Insights",
      description: "Receive profitable suggestions within seconds using AI analysis",
    },
    {
      icon: Target,
      title: "Beginner Friendly",
      description: "Designed for first-time investors with easy-to-follow guidance",
    },
  ];

  return (
    <div className="min-h-screen bg-background">
      <Navbar user={user} />
      
      {/* Hero Section */}
      <section className="relative pt-24 pb-20 overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src={heroBg} alt="" className="w-full h-full object-cover opacity-20" />
          <div className="absolute inset-0 bg-gradient-hero" />
        </div>
        
        <div className="container mx-auto px-4 relative z-10">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="text-5xl md:text-6xl font-bold mb-6 animate-fade-in">
              <span className="bg-gradient-primary bg-clip-text text-transparent">
                AI-Powered Stock
              </span>
              <br />
              Price Prediction
            </h1>
            <p className="text-xl text-muted-foreground mb-8 animate-fade-in" style={{ animationDelay: "0.1s" }}>
              Make smarter investment decisions with real-time analytics, AI predictions, and personalized insights designed for every investor.
            </p>
            <div className="flex gap-4 justify-center animate-fade-in" style={{ animationDelay: "0.2s" }}>
              <Button
                size="lg"
                onClick={() => navigate(user ? "/dashboard" : "/auth")}
                className="bg-gradient-primary hover:shadow-glow transition-all"
              >
                Start Predicting
              </Button>
              <Button
                size="lg"
                variant="outline"
                onClick={() => navigate("/chat")}
                className="border-primary/50 hover:bg-primary/10"
              >
                Try AI Assistant
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-card/30">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">
              Why Choose <span className="bg-gradient-primary bg-clip-text text-transparent">StockAI</span>?
            </h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Our platform combines cutting-edge AI technology with user-friendly design to help you navigate the stock market with confidence.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="bg-card/50 backdrop-blur-sm p-6 rounded-lg border border-border hover:border-primary/50 transition-all hover:shadow-card animate-fade-in"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="w-12 h-12 bg-gradient-primary rounded-lg flex items-center justify-center mb-4">
                  <feature.icon className="h-6 w-6 text-primary-foreground" />
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <div className="bg-gradient-primary rounded-2xl p-12 text-center">
            <h2 className="text-3xl md:text-4xl font-bold mb-4 text-primary-foreground">
              Ready to Transform Your Investing?
            </h2>
            <p className="text-primary-foreground/80 mb-8 max-w-2xl mx-auto">
              Join thousands of investors making data-driven decisions with our AI-powered platform.
            </p>
            <Button
              size="lg"
              onClick={() => navigate("/auth")}
              className="bg-background text-foreground hover:bg-background/90"
            >
              Get Started for Free
            </Button>
          </div>
        </div>
      </section>
    </div>
  );
}