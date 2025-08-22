import pandas as pd
import yfinance as yf

def get_financial_data(ticker="AAPL", period="6mo"):
    # a = financial structured data
    a = yf.download(ticker, period=period)
    return a

def get_macro_data():
    # b = simple macroeconomic data
    b = pd.DataFrame({
        "gdp_growth": [2.5, 3.0, 2.8, 2.0, 1.8, 2.2],
        "inflation": [4.0, 3.8, 3.5, 4.2, 4.5, 4.1],
        "label": [1, 1, 1, 0, 0, 1]
    })
    return b

def get_unstructured_events():
    # c = example event data
    c = ["Company posts strong quarterly earnings",
         "CEO warns about declining demand",
         "Debt restructuring announced"]
    return c
