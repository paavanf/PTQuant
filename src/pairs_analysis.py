import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

def hedge_ratio_ols(y, x):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    return model.params.iloc[1], model.params.iloc[0]


def rolling_hedge_ratio(y, x, window=60):
    betas = pd.Series(index=y.index, dtype=float)
    for i in range(window, len(y)+1):
        yi = y.iloc[i-window:i]
        xi = x.iloc[i-window:i]
        b, a = hedge_ratio_ols(yi, xi)
        betas.iloc[i-1] = b
    betas = betas.ffill()
    return betas

def cointegration_test(y, x):
    score, pvalue, _ = coint(y, x)
    return score, pvalue
