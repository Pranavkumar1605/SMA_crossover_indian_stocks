import pandas as pd
import numpy as np


def calculate_sma(df, short_window, long_window):

    df_copy = df.copy()

    df_copy[f"SMA_{short_window}"] = df_copy["Close"].rolling(window=short_window).mean()
    df_copy[f"SMA_{long_window}"] = df_copy["Close"].rolling(window=long_window).mean()

    print(f"Calculated SMA {short_window} and SMA {long_window}")

    return df_copy


def generate_signals(df):

    df_copy = df.copy()
    
    sma_columns = [col for col in df_copy.columns if col.startswith("SMA")]
    
    if len(sma_columns) < 2:
        raise ValueError("DataFrame must contain at least two SMA columns to generate signals.")
    
    sma_columns.sort()
    short_sma = sma_columns[0]
    long_sma = sma_columns[1]
    
    df_copy["Signal"] = 0

    df_copy["Position"] = np.where(df_copy[short_sma] > df_copy[long_sma], 1, -1)
    df_copy["Signal"] = df_copy["Position"].diff()

    buy_signals = len(df_copy[df_copy["Signal"] == 2])
    sell_signals = len(df_copy[df_copy["Signal"] == -2])

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

        df_SMA = calculate_sma(df, 10, 30)

        df_signals = generate_signals(df_SMA)
        

        print("Example of generated signals:")
        print(df_signals[[f"Close", "SMA_10", "SMA_30", "Position", "Signal"]].tail(10))

        print("module working correctly")
