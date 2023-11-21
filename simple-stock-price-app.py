import yfinance as yf
import streamlit as st
import requests

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol
tickerSymbol = 'GOOGL'

try:
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    
    # Get the historical prices for this ticker
    try:
        tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')
    except yf.errors.YFinanceError as yf_error:
        st.error(f"An error occurred while fetching data from yfinance: {yf_error}")
        st.stop()
except requests.exceptions.RequestException as req_error:
    st.error(f"An error occurred in the request to yfinance: {req_error}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

# Check if tickerDf is defined (no error occurred)
if 'tickerDf' in locals():
    # Open High Low Close Volume Dividends Stock Splits
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)
