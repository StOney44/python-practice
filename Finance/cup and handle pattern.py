import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def get_stock_data(ticker, period="2y"):
    """
    주식 데이터를 불러오는 함수
    """
    stock_data = yf.download(ticker, period=period)
    return stock_data

def find_cup_and_handle(stock_data):
    """
    Cup and Handle 패턴을 찾는 함수
    """
    stock_data['20d_MA'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['50d_MA'] = stock_data['Close'].rolling(window=50).mean()

    cup_and_handle_signals = []

    for i in range(len(stock_data) - 50):
        window = stock_data.iloc[i:i+50]
        low_price = window['Low'].min()
        high_price = window['High'].max()
        mid_price = (high_price + low_price) / 2

        if window['Close'].iloc[-1] > mid_price and window['Close'].iloc[-1] > window['50d_MA'].iloc[-1]:
            cup_and_handle_signals.append(i + 50)

    return cup_and_handle_signals

def find_low_cheat(stock_data):
    """
    Low Cheat 패턴을 찾는 함수
    """
    stock_data['20d_MA'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['50d_MA'] = stock_data['Close'].rolling(window=50).mean()

    low_cheat_signals = []

    for i in range(len(stock_data) - 30):
        window = stock_data.iloc[i:i+30]
        low_price = window['Low'].min()
        high_price = window['High'].max()
        mid_price = (high_price + low_price) / 2

        if window['Close'].iloc[-1] > mid_price and window['Close'].iloc[-1] > window['20d_MA'].iloc[-1]:
            low_cheat_signals.append(i + 30)

    return low_cheat_signals

def plot_signals(stock_data, signals, title):
    """
    신호를 시각화하는 함수
    """
    plt.figure(figsize=(14,7))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['20d_MA'], label='20d MA')
    plt.plot(stock_data['50d_MA'], label='50d MA')

    for signal in signals:
        plt.axvline(stock_data.index[signal], color='r', linestyle='--')

    plt.title(title)
    plt.legend()
    plt.show()

def main():
    ticker = input("Enter the stock ticker: ")
    stock_data = get_stock_data(ticker)

    cup_and_handle_signals = find_cup_and_handle(stock_data)
    low_cheat_signals = find_low_cheat(stock_data)

    plot_signals(stock_data, cup_and_handle_signals, f"Cup and Handle Signals for {ticker}")
    plot_signals(stock_data, low_cheat_signals, f"Low Cheat Signals for {ticker}")

if __name__ == "__main__":
    main()
