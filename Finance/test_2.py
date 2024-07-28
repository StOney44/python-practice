import yfinance as yf
import pandas as pd
import numpy as np

class PostpartumBleedingAnalyzer:
    def __init__(self, symbol, window_size):
        self.symbol = symbol
        self.window_size = window_size

    def fetch_data(self, start_date, end_date):
        stock = yf.Ticker(self.symbol)
        data = stock.history(start=start_date, end=end_date)
        return data

    def analyze_bleeding(self, data):
        data['High_Max'] = data['High'].rolling(window=self.window_size).max()
        data['Low_Min'] = data['Low'].rolling(window=self.window_size).min()
        data['Buy_Signal'] = data['Close'] > data['High_Max'].shift(1)
        data['Sell_Signal'] = data['Close'] < data['Low_Min'].shift(1)
        return data

    def run_analysis(self, start_date, end_date):
        df = self.fetch_data(start_date, end_date)
        analyzed_data = self.analyze_bleeding(df)

        bleeding_periods = []
        in_bleeding_period = False

        for index, row in analyzed_data.iterrows():
            if row['Buy_Signal'] and not in_bleeding_period:
                bleeding_periods.append((index, row['Close'], 'Start Bleeding'))
                in_bleeding_period = True
            elif row['Sell_Signal'] and in_bleeding_period:
                bleeding_periods.append((index, row['Close'], 'End Bleeding'))
                in_bleeding_period = False
        
        return bleeding_periods

class Interface:
    def __init__(self):
        self.symbol = ""
        self.window_size = 0

    def input_symbol(self):
        self.symbol = input("Enter the stock symbol: ")

    def input_window_size(self):
        self.window_size = int(input("Enter the window size for Donchian Channel: "))

    def input_date_range(self):
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        return start_date, end_date

    def run_analysis(self):
        bleeding_analyzer = PostpartumBleedingAnalyzer(self.symbol, self.window_size)
        start_date, end_date = self.input_date_range()
        bleeding_periods = bleeding_analyzer.run_analysis(start_date, end_date)

        print("Postpartum Bleeding Analysis Results:")
        for period in bleeding_periods:
            print(period)

if __name__ == "__main__":
    interface = Interface()
    interface.input_symbol()
    interface.input_window_size()
    interface.run_analysis()
