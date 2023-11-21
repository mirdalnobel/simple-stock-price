import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol
tickerSymbol = 'GOOGL'
# Get data on this ticker
try:
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')
except yf.errors.YFinanceError as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
