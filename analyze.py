"""
Simple stock analysis: fetch daily prices and compute moving averages.

Usage:
    pip install requests pandas
    export ALPHAVANTAGE_API_KEY=your_key_here
    python scripts/analyze.py AAPL
"""

import os
import sys

import pandas as pd
import requests

API_URL = "https://www.alphavantage.co/query"


def fetch_daily_prices(symbol: str, api_key: str) -> pd.DataFrame:
    """Fetch daily closing prices for a symbol from Alpha Vantage."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact",  # last ~100 days
    }
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json().get("Time Series (Daily)")
    if not data:
        raise ValueError("No data returned — check your API key or symbol.")

    df = pd.DataFrame.from_dict(data, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df["close"] = df["4. close"].astype(float)
    return df[["close"]]


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple moving averages and daily % change."""
    df["sma_20"] = df["close"].rolling(20).mean()
    df["sma_50"] = df["close"].rolling(50).mean()
    df["pct_change"] = df["close"].pct_change() * 100
    return df


def main():
    symbol = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        sys.exit("Set the ALPHAVANTAGE_API_KEY environment variable first.")

    df = add_indicators(fetch_daily_prices(symbol, api_key))
    latest = df.iloc[-1]

    print(f"\n{symbol} — latest analysis ({df.index[-1].date()})")
    print(f"  Close:        ${latest['close']:.2f}")
    print(f"  Day change:   {latest['pct_change']:+.2f}%")
    print(f"  20-day SMA:   ${latest['sma_20']:.2f}")
    print(f"  50-day SMA:   ${latest['sma_50']:.2f}")

    if latest["sma_20"] > latest["sma_50"]:
        print("  Trend:        Short-term above long-term (bullish-leaning)")
    else:
        print("  Trend:        Short-term below long-term (bearish-leaning)")


if __name__ == "__main__":
    main()
