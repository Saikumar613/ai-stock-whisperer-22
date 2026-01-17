# Comprehensive Stock Symbols Dataset
# Contains major companies from NYSE, NASDAQ, and other exchanges

STOCK_SYMBOLS = {
    # Technology Giants
    "AAPL": {"name": "Apple Inc.", "sector": "Technology"},
    "MSFT": {"name": "Microsoft Corporation", "sector": "Technology"},
    "GOOGL": {"name": "Alphabet Inc. Class A", "sector": "Technology"},
    "GOOG": {"name": "Alphabet Inc. Class C", "sector": "Technology"},
    "AMZN": {"name": "Amazon.com Inc.", "sector": "Consumer Cyclical"},
    "META": {"name": "Meta Platforms Inc.", "sector": "Technology"},
    "NVDA": {"name": "NVIDIA Corporation", "sector": "Technology"},
    "TSLA": {"name": "Tesla Inc.", "sector": "Consumer Cyclical"},
    "AMD": {"name": "Advanced Micro Devices", "sector": "Technology"},
    "INTC": {"name": "Intel Corporation", "sector": "Technology"},
    "CRM": {"name": "Salesforce Inc.", "sector": "Technology"},
    "ORCL": {"name": "Oracle Corporation", "sector": "Technology"},
    "ADBE": {"name": "Adobe Inc.", "sector": "Technology"},
    "CSCO": {"name": "Cisco Systems Inc.", "sector": "Technology"},
    "IBM": {"name": "IBM Corporation", "sector": "Technology"},
    "QCOM": {"name": "Qualcomm Inc.", "sector": "Technology"},
    "TXN": {"name": "Texas Instruments", "sector": "Technology"},
    "AVGO": {"name": "Broadcom Inc.", "sector": "Technology"},
    "NOW": {"name": "ServiceNow Inc.", "sector": "Technology"},
    "SHOP": {"name": "Shopify Inc.", "sector": "Technology"},
    "SQ": {"name": "Block Inc.", "sector": "Technology"},
    "PYPL": {"name": "PayPal Holdings", "sector": "Technology"},
    "UBER": {"name": "Uber Technologies", "sector": "Technology"},
    "LYFT": {"name": "Lyft Inc.", "sector": "Technology"},
    "SNAP": {"name": "Snap Inc.", "sector": "Technology"},
    "PINS": {"name": "Pinterest Inc.", "sector": "Technology"},
    "SPOT": {"name": "Spotify Technology", "sector": "Technology"},
    "NFLX": {"name": "Netflix Inc.", "sector": "Communication Services"},
    "DIS": {"name": "Walt Disney Company", "sector": "Communication Services"},
    "CMCSA": {"name": "Comcast Corporation", "sector": "Communication Services"},
    
    # Financial Services
    "JPM": {"name": "JPMorgan Chase & Co.", "sector": "Financial Services"},
    "BAC": {"name": "Bank of America Corp.", "sector": "Financial Services"},
    "WFC": {"name": "Wells Fargo & Company", "sector": "Financial Services"},
    "C": {"name": "Citigroup Inc.", "sector": "Financial Services"},
    "GS": {"name": "Goldman Sachs Group", "sector": "Financial Services"},
    "MS": {"name": "Morgan Stanley", "sector": "Financial Services"},
    "BLK": {"name": "BlackRock Inc.", "sector": "Financial Services"},
    "SCHW": {"name": "Charles Schwab Corp.", "sector": "Financial Services"},
    "AXP": {"name": "American Express Co.", "sector": "Financial Services"},
    "V": {"name": "Visa Inc.", "sector": "Financial Services"},
    "MA": {"name": "Mastercard Inc.", "sector": "Financial Services"},
    "COF": {"name": "Capital One Financial", "sector": "Financial Services"},
    "USB": {"name": "U.S. Bancorp", "sector": "Financial Services"},
    "PNC": {"name": "PNC Financial Services", "sector": "Financial Services"},
    "TFC": {"name": "Truist Financial Corp.", "sector": "Financial Services"},
    
    # Healthcare & Pharmaceuticals
    "JNJ": {"name": "Johnson & Johnson", "sector": "Healthcare"},
    "UNH": {"name": "UnitedHealth Group", "sector": "Healthcare"},
    "PFE": {"name": "Pfizer Inc.", "sector": "Healthcare"},
    "ABBV": {"name": "AbbVie Inc.", "sector": "Healthcare"},
    "MRK": {"name": "Merck & Co. Inc.", "sector": "Healthcare"},
    "LLY": {"name": "Eli Lilly and Company", "sector": "Healthcare"},
    "TMO": {"name": "Thermo Fisher Scientific", "sector": "Healthcare"},
    "ABT": {"name": "Abbott Laboratories", "sector": "Healthcare"},
    "DHR": {"name": "Danaher Corporation", "sector": "Healthcare"},
    "BMY": {"name": "Bristol-Myers Squibb", "sector": "Healthcare"},
    "AMGN": {"name": "Amgen Inc.", "sector": "Healthcare"},
    "GILD": {"name": "Gilead Sciences Inc.", "sector": "Healthcare"},
    "CVS": {"name": "CVS Health Corporation", "sector": "Healthcare"},
    "CI": {"name": "Cigna Group", "sector": "Healthcare"},
    "ISRG": {"name": "Intuitive Surgical", "sector": "Healthcare"},
    "VRTX": {"name": "Vertex Pharmaceuticals", "sector": "Healthcare"},
    "REGN": {"name": "Regeneron Pharmaceuticals", "sector": "Healthcare"},
    "MRNA": {"name": "Moderna Inc.", "sector": "Healthcare"},
    "BIIB": {"name": "Biogen Inc.", "sector": "Healthcare"},
    
    # Consumer Goods & Retail
    "WMT": {"name": "Walmart Inc.", "sector": "Consumer Defensive"},
    "PG": {"name": "Procter & Gamble Co.", "sector": "Consumer Defensive"},
    "KO": {"name": "Coca-Cola Company", "sector": "Consumer Defensive"},
    "PEP": {"name": "PepsiCo Inc.", "sector": "Consumer Defensive"},
    "COST": {"name": "Costco Wholesale Corp.", "sector": "Consumer Defensive"},
    "HD": {"name": "Home Depot Inc.", "sector": "Consumer Cyclical"},
    "LOW": {"name": "Lowe's Companies Inc.", "sector": "Consumer Cyclical"},
    "NKE": {"name": "Nike Inc.", "sector": "Consumer Cyclical"},
    "MCD": {"name": "McDonald's Corporation", "sector": "Consumer Cyclical"},
    "SBUX": {"name": "Starbucks Corporation", "sector": "Consumer Cyclical"},
    "TGT": {"name": "Target Corporation", "sector": "Consumer Defensive"},
    "MDLZ": {"name": "Mondelez International", "sector": "Consumer Defensive"},
    "CL": {"name": "Colgate-Palmolive Co.", "sector": "Consumer Defensive"},
    "EL": {"name": "Estee Lauder Companies", "sector": "Consumer Defensive"},
    "KMB": {"name": "Kimberly-Clark Corp.", "sector": "Consumer Defensive"},
    "GIS": {"name": "General Mills Inc.", "sector": "Consumer Defensive"},
    "K": {"name": "Kellanova", "sector": "Consumer Defensive"},
    "HSY": {"name": "Hershey Company", "sector": "Consumer Defensive"},
    "KHC": {"name": "Kraft Heinz Company", "sector": "Consumer Defensive"},
    "STZ": {"name": "Constellation Brands", "sector": "Consumer Defensive"},
    "TAP": {"name": "Molson Coors Beverage", "sector": "Consumer Defensive"},
    "BUD": {"name": "Anheuser-Busch InBev", "sector": "Consumer Defensive"},
    
    # Energy
    "XOM": {"name": "Exxon Mobil Corporation", "sector": "Energy"},
    "CVX": {"name": "Chevron Corporation", "sector": "Energy"},
    "COP": {"name": "ConocoPhillips", "sector": "Energy"},
    "SLB": {"name": "Schlumberger Limited", "sector": "Energy"},
    "EOG": {"name": "EOG Resources Inc.", "sector": "Energy"},
    "PXD": {"name": "Pioneer Natural Resources", "sector": "Energy"},
    "MPC": {"name": "Marathon Petroleum Corp.", "sector": "Energy"},
    "PSX": {"name": "Phillips 66", "sector": "Energy"},
    "VLO": {"name": "Valero Energy Corp.", "sector": "Energy"},
    "OXY": {"name": "Occidental Petroleum", "sector": "Energy"},
    "HAL": {"name": "Halliburton Company", "sector": "Energy"},
    "BKR": {"name": "Baker Hughes Company", "sector": "Energy"},
    "DVN": {"name": "Devon Energy Corp.", "sector": "Energy"},
    "FANG": {"name": "Diamondback Energy", "sector": "Energy"},
    
    # Industrials
    "CAT": {"name": "Caterpillar Inc.", "sector": "Industrials"},
    "DE": {"name": "Deere & Company", "sector": "Industrials"},
    "BA": {"name": "Boeing Company", "sector": "Industrials"},
    "HON": {"name": "Honeywell International", "sector": "Industrials"},
    "UPS": {"name": "United Parcel Service", "sector": "Industrials"},
    "FDX": {"name": "FedEx Corporation", "sector": "Industrials"},
    "LMT": {"name": "Lockheed Martin Corp.", "sector": "Industrials"},
    "RTX": {"name": "RTX Corporation", "sector": "Industrials"},
    "GE": {"name": "General Electric Co.", "sector": "Industrials"},
    "MMM": {"name": "3M Company", "sector": "Industrials"},
    "GD": {"name": "General Dynamics Corp.", "sector": "Industrials"},
    "NOC": {"name": "Northrop Grumman Corp.", "sector": "Industrials"},
    "UNP": {"name": "Union Pacific Corp.", "sector": "Industrials"},
    "CSX": {"name": "CSX Corporation", "sector": "Industrials"},
    "NSC": {"name": "Norfolk Southern Corp.", "sector": "Industrials"},
    "EMR": {"name": "Emerson Electric Co.", "sector": "Industrials"},
    "ETN": {"name": "Eaton Corporation", "sector": "Industrials"},
    "ITW": {"name": "Illinois Tool Works", "sector": "Industrials"},
    "PH": {"name": "Parker-Hannifin Corp.", "sector": "Industrials"},
    "ROK": {"name": "Rockwell Automation", "sector": "Industrials"},
    
    # Real Estate
    "AMT": {"name": "American Tower Corp.", "sector": "Real Estate"},
    "PLD": {"name": "Prologis Inc.", "sector": "Real Estate"},
    "CCI": {"name": "Crown Castle Inc.", "sector": "Real Estate"},
    "EQIX": {"name": "Equinix Inc.", "sector": "Real Estate"},
    "SPG": {"name": "Simon Property Group", "sector": "Real Estate"},
    "PSA": {"name": "Public Storage", "sector": "Real Estate"},
    "O": {"name": "Realty Income Corp.", "sector": "Real Estate"},
    "WELL": {"name": "Welltower Inc.", "sector": "Real Estate"},
    "AVB": {"name": "AvalonBay Communities", "sector": "Real Estate"},
    "EQR": {"name": "Equity Residential", "sector": "Real Estate"},
    "DLR": {"name": "Digital Realty Trust", "sector": "Real Estate"},
    "VTR": {"name": "Ventas Inc.", "sector": "Real Estate"},
    
    # Utilities
    "NEE": {"name": "NextEra Energy Inc.", "sector": "Utilities"},
    "DUK": {"name": "Duke Energy Corp.", "sector": "Utilities"},
    "SO": {"name": "Southern Company", "sector": "Utilities"},
    "D": {"name": "Dominion Energy Inc.", "sector": "Utilities"},
    "AEP": {"name": "American Electric Power", "sector": "Utilities"},
    "EXC": {"name": "Exelon Corporation", "sector": "Utilities"},
    "SRE": {"name": "Sempra", "sector": "Utilities"},
    "XEL": {"name": "Xcel Energy Inc.", "sector": "Utilities"},
    "ED": {"name": "Consolidated Edison", "sector": "Utilities"},
    "WEC": {"name": "WEC Energy Group", "sector": "Utilities"},
    "ES": {"name": "Eversource Energy", "sector": "Utilities"},
    "AWK": {"name": "American Water Works", "sector": "Utilities"},
    
    # Materials
    "LIN": {"name": "Linde plc", "sector": "Materials"},
    "APD": {"name": "Air Products & Chemicals", "sector": "Materials"},
    "SHW": {"name": "Sherwin-Williams Co.", "sector": "Materials"},
    "ECL": {"name": "Ecolab Inc.", "sector": "Materials"},
    "FCX": {"name": "Freeport-McMoRan Inc.", "sector": "Materials"},
    "NEM": {"name": "Newmont Corporation", "sector": "Materials"},
    "NUE": {"name": "Nucor Corporation", "sector": "Materials"},
    "DOW": {"name": "Dow Inc.", "sector": "Materials"},
    "DD": {"name": "DuPont de Nemours", "sector": "Materials"},
    "PPG": {"name": "PPG Industries Inc.", "sector": "Materials"},
    "VMC": {"name": "Vulcan Materials Co.", "sector": "Materials"},
    "MLM": {"name": "Martin Marietta Materials", "sector": "Materials"},
    
    # Automotive
    "F": {"name": "Ford Motor Company", "sector": "Consumer Cyclical"},
    "GM": {"name": "General Motors Company", "sector": "Consumer Cyclical"},
    "TM": {"name": "Toyota Motor Corp.", "sector": "Consumer Cyclical"},
    "HMC": {"name": "Honda Motor Co.", "sector": "Consumer Cyclical"},
    "RIVN": {"name": "Rivian Automotive", "sector": "Consumer Cyclical"},
    "LCID": {"name": "Lucid Group Inc.", "sector": "Consumer Cyclical"},
    
    # Airlines & Travel
    "DAL": {"name": "Delta Air Lines Inc.", "sector": "Industrials"},
    "UAL": {"name": "United Airlines Holdings", "sector": "Industrials"},
    "AAL": {"name": "American Airlines Group", "sector": "Industrials"},
    "LUV": {"name": "Southwest Airlines Co.", "sector": "Industrials"},
    "MAR": {"name": "Marriott International", "sector": "Consumer Cyclical"},
    "HLT": {"name": "Hilton Worldwide Holdings", "sector": "Consumer Cyclical"},
    "ABNB": {"name": "Airbnb Inc.", "sector": "Consumer Cyclical"},
    "BKNG": {"name": "Booking Holdings Inc.", "sector": "Consumer Cyclical"},
    "EXPE": {"name": "Expedia Group Inc.", "sector": "Consumer Cyclical"},
    
    # Semiconductors
    "TSM": {"name": "Taiwan Semiconductor", "sector": "Technology"},
    "ASML": {"name": "ASML Holding NV", "sector": "Technology"},
    "MU": {"name": "Micron Technology", "sector": "Technology"},
    "LRCX": {"name": "Lam Research Corp.", "sector": "Technology"},
    "AMAT": {"name": "Applied Materials Inc.", "sector": "Technology"},
    "KLAC": {"name": "KLA Corporation", "sector": "Technology"},
    "MRVL": {"name": "Marvell Technology", "sector": "Technology"},
    "ON": {"name": "ON Semiconductor Corp.", "sector": "Technology"},
    "NXPI": {"name": "NXP Semiconductors", "sector": "Technology"},
    "ADI": {"name": "Analog Devices Inc.", "sector": "Technology"},
    "SWKS": {"name": "Skyworks Solutions", "sector": "Technology"},
    "MPWR": {"name": "Monolithic Power Systems", "sector": "Technology"},
    
    # Cybersecurity & Cloud
    "PANW": {"name": "Palo Alto Networks", "sector": "Technology"},
    "CRWD": {"name": "CrowdStrike Holdings", "sector": "Technology"},
    "FTNT": {"name": "Fortinet Inc.", "sector": "Technology"},
    "ZS": {"name": "Zscaler Inc.", "sector": "Technology"},
    "OKTA": {"name": "Okta Inc.", "sector": "Technology"},
    "NET": {"name": "Cloudflare Inc.", "sector": "Technology"},
    "DDOG": {"name": "Datadog Inc.", "sector": "Technology"},
    "SNOW": {"name": "Snowflake Inc.", "sector": "Technology"},
    "MDB": {"name": "MongoDB Inc.", "sector": "Technology"},
    "TEAM": {"name": "Atlassian Corp.", "sector": "Technology"},
    "WDAY": {"name": "Workday Inc.", "sector": "Technology"},
    "SPLK": {"name": "Splunk Inc.", "sector": "Technology"},
    
    # Gaming & Entertainment
    "ATVI": {"name": "Activision Blizzard", "sector": "Communication Services"},
    "EA": {"name": "Electronic Arts Inc.", "sector": "Communication Services"},
    "TTWO": {"name": "Take-Two Interactive", "sector": "Communication Services"},
    "RBLX": {"name": "Roblox Corporation", "sector": "Communication Services"},
    "PARA": {"name": "Paramount Global", "sector": "Communication Services"},
    "WBD": {"name": "Warner Bros. Discovery", "sector": "Communication Services"},
    "LYV": {"name": "Live Nation Entertainment", "sector": "Communication Services"},
    
    # E-commerce & Delivery
    "EBAY": {"name": "eBay Inc.", "sector": "Consumer Cyclical"},
    "ETSY": {"name": "Etsy Inc.", "sector": "Consumer Cyclical"},
    "W": {"name": "Wayfair Inc.", "sector": "Consumer Cyclical"},
    "CHWY": {"name": "Chewy Inc.", "sector": "Consumer Cyclical"},
    "DASH": {"name": "DoorDash Inc.", "sector": "Consumer Cyclical"},
    "GRUB": {"name": "Grubhub Inc.", "sector": "Consumer Cyclical"},
    
    # Telecom
    "T": {"name": "AT&T Inc.", "sector": "Communication Services"},
    "VZ": {"name": "Verizon Communications", "sector": "Communication Services"},
    "TMUS": {"name": "T-Mobile US Inc.", "sector": "Communication Services"},
    
    # Insurance
    "BRK-B": {"name": "Berkshire Hathaway B", "sector": "Financial Services"},
    "BRK-A": {"name": "Berkshire Hathaway A", "sector": "Financial Services"},
    "PGR": {"name": "Progressive Corp.", "sector": "Financial Services"},
    "TRV": {"name": "Travelers Companies", "sector": "Financial Services"},
    "ALL": {"name": "Allstate Corporation", "sector": "Financial Services"},
    "MET": {"name": "MetLife Inc.", "sector": "Financial Services"},
    "PRU": {"name": "Prudential Financial", "sector": "Financial Services"},
    "AFL": {"name": "Aflac Incorporated", "sector": "Financial Services"},
    "AIG": {"name": "American International", "sector": "Financial Services"},
    "CB": {"name": "Chubb Limited", "sector": "Financial Services"},
    
    # Additional Popular Stocks
    "COIN": {"name": "Coinbase Global Inc.", "sector": "Financial Services"},
    "HOOD": {"name": "Robinhood Markets", "sector": "Financial Services"},
    "PLTR": {"name": "Palantir Technologies", "sector": "Technology"},
    "PATH": {"name": "UiPath Inc.", "sector": "Technology"},
    "DOCU": {"name": "DocuSign Inc.", "sector": "Technology"},
    "ZM": {"name": "Zoom Video Communications", "sector": "Technology"},
    "TWLO": {"name": "Twilio Inc.", "sector": "Technology"},
    "U": {"name": "Unity Software Inc.", "sector": "Technology"},
    "AI": {"name": "C3.ai Inc.", "sector": "Technology"},
    "SOFI": {"name": "SoFi Technologies", "sector": "Financial Services"},
    "AFRM": {"name": "Affirm Holdings", "sector": "Financial Services"},
    "UPST": {"name": "Upstart Holdings", "sector": "Financial Services"},
    
    # ETFs (Exchange Traded Funds)
    "SPY": {"name": "SPDR S&P 500 ETF", "sector": "ETF"},
    "QQQ": {"name": "Invesco QQQ Trust", "sector": "ETF"},
    "IWM": {"name": "iShares Russell 2000", "sector": "ETF"},
    "DIA": {"name": "SPDR Dow Jones ETF", "sector": "ETF"},
    "VTI": {"name": "Vanguard Total Stock", "sector": "ETF"},
    "VOO": {"name": "Vanguard S&P 500 ETF", "sector": "ETF"},
    "VXX": {"name": "iPath Series B S&P VIX", "sector": "ETF"},
    "GLD": {"name": "SPDR Gold Shares", "sector": "ETF"},
    "SLV": {"name": "iShares Silver Trust", "sector": "ETF"},
    "USO": {"name": "United States Oil Fund", "sector": "ETF"},
    "XLF": {"name": "Financial Select Sector", "sector": "ETF"},
    "XLK": {"name": "Technology Select Sector", "sector": "ETF"},
    "XLE": {"name": "Energy Select Sector", "sector": "ETF"},
    "XLV": {"name": "Health Care Select Sector", "sector": "ETF"},
    "ARKK": {"name": "ARK Innovation ETF", "sector": "ETF"},
    "ARKG": {"name": "ARK Genomic Revolution", "sector": "ETF"},
    
    # International Stocks (ADRs)
    "BABA": {"name": "Alibaba Group Holding", "sector": "Consumer Cyclical"},
    "JD": {"name": "JD.com Inc.", "sector": "Consumer Cyclical"},
    "PDD": {"name": "PDD Holdings Inc.", "sector": "Consumer Cyclical"},
    "BIDU": {"name": "Baidu Inc.", "sector": "Communication Services"},
    "NIO": {"name": "NIO Inc.", "sector": "Consumer Cyclical"},
    "XPEV": {"name": "XPeng Inc.", "sector": "Consumer Cyclical"},
    "LI": {"name": "Li Auto Inc.", "sector": "Consumer Cyclical"},
    "SE": {"name": "Sea Limited", "sector": "Consumer Cyclical"},
    "GRAB": {"name": "Grab Holdings", "sector": "Technology"},
    "SAP": {"name": "SAP SE", "sector": "Technology"},
    "SONY": {"name": "Sony Group Corporation", "sector": "Consumer Cyclical"},
    "MELI": {"name": "MercadoLibre Inc.", "sector": "Consumer Cyclical"},
    "NU": {"name": "Nu Holdings Ltd.", "sector": "Financial Services"},
    "UL": {"name": "Unilever PLC", "sector": "Consumer Defensive"},
    "NVO": {"name": "Novo Nordisk A/S", "sector": "Healthcare"},
    "AZN": {"name": "AstraZeneca PLC", "sector": "Healthcare"},
    "GSK": {"name": "GSK plc", "sector": "Healthcare"},
    "SNY": {"name": "Sanofi", "sector": "Healthcare"},
    "HSBC": {"name": "HSBC Holdings plc", "sector": "Financial Services"},
    "RY": {"name": "Royal Bank of Canada", "sector": "Financial Services"},
    "TD": {"name": "Toronto-Dominion Bank", "sector": "Financial Services"},
    "BMO": {"name": "Bank of Montreal", "sector": "Financial Services"},
    "BNS": {"name": "Bank of Nova Scotia", "sector": "Financial Services"},
    "CM": {"name": "Canadian Imperial Bank", "sector": "Financial Services"},
    "SHOP": {"name": "Shopify Inc.", "sector": "Technology"},
    "ENB": {"name": "Enbridge Inc.", "sector": "Energy"},
    "CNQ": {"name": "Canadian Natural Resources", "sector": "Energy"},
    "SU": {"name": "Suncor Energy Inc.", "sector": "Energy"},
    "BP": {"name": "BP p.l.c.", "sector": "Energy"},
    "SHEL": {"name": "Shell plc", "sector": "Energy"},
    "TTE": {"name": "TotalEnergies SE", "sector": "Energy"},
    "EQNR": {"name": "Equinor ASA", "sector": "Energy"},
    "RIO": {"name": "Rio Tinto Group", "sector": "Materials"},
    "BHP": {"name": "BHP Group Limited", "sector": "Materials"},
    "VALE": {"name": "Vale S.A.", "sector": "Materials"},
}

# Helper functions
def get_all_symbols():
    """Return list of all stock symbols"""
    return list(STOCK_SYMBOLS.keys())

def get_symbols_by_sector(sector):
    """Return list of symbols for a specific sector"""
    return [symbol for symbol, info in STOCK_SYMBOLS.items() if info["sector"] == sector]

def get_stock_info(symbol):
    """Get stock info by symbol"""
    return STOCK_SYMBOLS.get(symbol.upper())

def get_all_sectors():
    """Return list of unique sectors"""
    return list(set(info["sector"] for info in STOCK_SYMBOLS.values()))

def search_stocks(query):
    """Search stocks by name or symbol"""
    query = query.upper()
    results = {}
    for symbol, info in STOCK_SYMBOLS.items():
        if query in symbol or query.lower() in info["name"].lower():
            results[symbol] = info
    return results

# Total count
TOTAL_STOCKS = len(STOCK_SYMBOLS)

if __name__ == "__main__":
    print(f"Total stocks in database: {TOTAL_STOCKS}")
    print(f"Sectors: {get_all_sectors()}")
