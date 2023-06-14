import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime


def get_stock_data(ticker_symbol, period, start, end):
    """Gets the historical stock data for a given ticker symbol."""
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period=period, start=start, end=end)
    return ticker_df


def main():
    """The main function."""

    st.write("""
    # Simple Stock Price App

    Shown are the stock **closing price** and **volume** of Google!

    """)

    # Get the ticker symbol from the user.
    ticker_symbol = st.sidebar.text_input("Enter a stock symbol: ", value="GOOGL")

    # Get the period from the user.
    period = st.sidebar.selectbox("Select a period: ", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "1wk"])

    # Get the start date from the user.
    start = st.sidebar.date_input("Select a start date: ", value=datetime(2010, 5, 31))

    # Get the end date from the user.
    end = st.sidebar.date_input("Select an end date: ", value=datetime(2020, 5, 31))

    # Get the stock data for the ticker symbol.
    ticker_df = get_stock_data(ticker_symbol, period, start, end)

    # Plot the closing price and volume of the stock.
    st.subheader("Closing Price")
    st.line_chart(ticker_df.Close)

    st.subheader("Volume")
    st.line_chart(ticker_df.Volume)


if __name__ == "__main__":
    main()


# import streamlit as st
# import pandas as pd
# import yfinance as yf

# st.write("""
# # Simple Stock Price App

# Shown are the stock **closing price** and **volume** of Google!

# """)

# # define the ticker symbol
# ticker_symbol = 'GOOGL'

# # get data on this ticker
# ticker_data = yf.Ticker(ticker_symbol)

# # get the fistorical prices for this ticker
# ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

# st.subheader("Closing Price")
# st.line_chart(ticker_df.Close)

# st.subheader("Volume")
# st.line_chart(ticker_df.Volume)





