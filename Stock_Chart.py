import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
ticker = 'AAPL'


data = yf.download(ticker, period='30d')


if isinstance(data.columns, pd.MultiIndex):
    close_prices = data['Close'][ticker].dropna()
else:
    close_prices = data['Close'].dropna()


if not close_prices.empty:
    print(f"\nStock: {ticker}")
    print(f"Minimum Close Price: {float(close_prices.min()):.2f}")
    print(f"Maximum Close Price: {float(close_prices.max()):.2f}")
    print(f"Average Close Price: {float(close_prices.mean()):.2f}")

    plt.figure(figsize=(10, 5))
    plt.plot(close_prices.index, close_prices, label='Close Price', color='blue')
    plt.title(f'{ticker} Stock Closing Prices - Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("No closing price data available.")
