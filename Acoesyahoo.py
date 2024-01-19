import yfinance as yf 

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("2y")
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split("-")[0]
    return df

btc = carregar_dados('BTC-USD')
eth = carregar_dados('ETH-USD')
sol = carregar_dados('SOL-USD')
dodge = carregar_dados('DOGE-USD')
xrp = carregar_dados('XRP-USD')
btc.head()
eth.head()
sol.head()
dodge.head()
xrp.head()