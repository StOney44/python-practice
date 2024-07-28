import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock_data = yf.download(ticker, start="2010-01-01")
    stock_data['50d_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200d_MA'] = stock_data['Close'].rolling(window=200).mean()
    return stock_data

def find_cup_and_handle(stock_data):
    stock_data['High_Price'] = stock_data['Close'].rolling(window=20).max()
    stock_data['Low_Price'] = stock_data['Close'].rolling(window=20).min()

    conditions = [
        (stock_data['Close'].shift(-1) > stock_data['High_Price']),
        (stock_data['Close'] > stock_data['50d_MA']),
        (stock_data['Close'] > stock_data['200d_MA'])
    ]

    stock_data['Cup_and_Handle'] = 0
    stock_data.loc[conditions[0] & conditions[1] & conditions[2], 'Cup_and_Handle'] = 1

    return stock_data[stock_data['Cup_and_Handle'] == 1]

ticker = "AAPL"
stock_data = get_stock_data(ticker)
cup_and_handle_signals = find_cup_and_handle(stock_data)

print(cup_and_handle_signals)
