import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


def download_stock_data(ticker, period="5y", interval="1d"):

    print(f"\nDownloading data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    if df.empty:
        print(f"No data found for {ticker}.")
        return None

    print(f"\nSuccesfully downloaded {len(df)} rows of data")
    print(f"\nDate range: {df.index[0].date()} to {df.index[-1].date()}")

    return df


# data = download_stock_data("RELIANCE.NS", period="5y", interval="1d")


def get_data_info(df):

    print("\n" + "=" * 50)
    print("Data Information")
    print("=" * 50)

    print(f"Total rows:{len(df)}")
    print(f"Date range: {df.index[0].date()} to {df.index[-1].date()}")

    print(f"\n columns: {list(df.columns)}")

    missing = df.isnull().sum()
    print(f"\n Missing values: {missing}")

    print(df.head())

    print("\n Basic Satatistics")
    print(df.describe())


# print(get_data_info(data))

if __name__ == "__main__":

    ticker = "RELIANCE.NS"
    df = download_stock_data(ticker, period="5y", interval="1d")

    if df is not None:
        print(get_data_info(df))
    else:
        print("Download failed")
