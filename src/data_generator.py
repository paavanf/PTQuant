import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_cointegrated_pair(n_days=1000, seed=42, beta=1.25, sigma_noise=0.5):
    np.random.seed(seed)
    start = datetime.today() - timedelta(days=n_days)
    dates = pd.bdate_range(start, periods=n_days)
    eps_x = np.random.normal(scale=1.0, size=n_days)
    x = np.cumsum(eps_x) + 50
    phi = 0.95
    z = np.zeros(n_days)
    for t in range(1, n_days):
        z[t] = phi*z[t-1] + np.random.normal(scale=sigma_noise)
    alpha = 2.0
    y = alpha + beta*x + z
    df = pd.DataFrame({'Date': dates, 'X': x, 'Y': y}).set_index('Date')
    df_out1 = df[['X']].rename(columns={'X':'Close'})
    df_out2 = df[['Y']].rename(columns={'Y':'Close'})
    return df_out1, df_out2

if __name__ == '__main__':
    s1, s2 = generate_cointegrated_pair(1000)
    s1.to_csv('data/stockA.csv', index=True)
    s2.to_csv('data/stockB.csv', index=True)
