import pandas as pd

def combine_data(a, b):
    # Create return feature
    a["return"] = a["Adj Close"].pct_change()
    a = a.dropna()

    # Merge with macroeconomic data
    d = pd.DataFrame({
        "return": a["return"].tail(len(b)).values,
        "gdp_growth": b["gdp_growth"],
        "inflation": b["inflation"],
        "label": b["label"]
    })
    return d
