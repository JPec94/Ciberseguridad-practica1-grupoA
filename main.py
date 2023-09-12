from yahoo_data_fecther import get_price

tickers = ["KO", "DIS", "PEP", "INTC", "F", "V"]

for t in tickers:
    get_price(ticker=t, verbose=True)
