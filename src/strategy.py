import pandas as pd
import numpy as np


def calculate_sma(df, short_window=20, long_window=50):

    df_copy = df.copy()

    df_copy["SMA_20"] = df_copy["Close"].rolling(window=short_window).mean()
    df_copy["SMA_50"] = df_copy["Close"].rolling(window=long_window).mean()

    print(f"Calculated SMA {short_window} and SMA {long_window}")

    return df_copy


def generate_signals(df):

    df_copy = df.copy()

    df_copy["Signal"] = 0

    df_copy["Position"] = np.where(df_copy["SMA_20"] > df_copy["SMA_50"], 1, 0)
    df_copy["Signal"] = df_copy["Position"].diff()

    buy_signals = len(df_copy[df_copy["Signal"] == 1])
    sell_signals = len(df_copy[df_copy["Signal"] == -1])

    print(f"Buy signals:{buy_signals}")
    print(f"Sell signals:{sell_signals}")

    return df_copy


if __name__ == "__main__":

    import sys

    sys.path.append(".")
    from src.data_loader import download_stock_data

    print("testing strategy module")

    ticker = "RELIANCE.NS"
    df = download_stock_data(ticker, period="5y", interval="1d")

    if df is not None:

        df_SMA = calculate_sma(df, short_window=20, long_window=50)

        df_signals = generate_signals(df_SMA)

        print("Example of generated signals:")
        print(df_signals[["Close", "SMA_20", "SMA_50", "Position", "Signal"]].tail(10))

        print("module working correctly")
