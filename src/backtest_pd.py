import numpy as np
import pandas as pd

def zscore(series, window):
    mu = series.rolling(window).mean()
    sigma = series.rolling(window).std()
    return (series - mu) / sigma

def generate_signals(spread_z, entry_z=2.0, exit_z=0.0):
    position = 0
    positions = []
    for z in spread_z:
        if position == 0:
            if z > entry_z:
                position = -1
            elif z < -entry_z:
                position = 1
        elif position == 1:
            if z >= exit_z:
                position = 0
        elif position == -1:
            if z <= exit_z:
                position = 0
        positions.append(position)
    return pd.Series(positions, index=spread_z.index)

def backtest_pair(prices_a, prices_b, hedge_ratio, signals):
    returns_a = prices_a['Close'].pct_change().fillna(0)
    returns_b = prices_b['Close'].pct_change().fillna(0)
    pnl = signals.shift(1) * (returns_a - hedge_ratio.shift(1) * returns_b)
    pnl = pnl.fillna(0)
    cum_ret = (1 + pnl).cumprod()
    stats = {}
    stats['total_return'] = cum_ret.iloc[-1] - 1
    ann_factor = 252
    stats['annual_return'] = (1 + stats['total_return']) ** (ann_factor/len(pnl)) - 1
    stats['sharpe'] = (pnl.mean() / pnl.std()) * np.sqrt(ann_factor) if pnl.std() != 0 else np.nan
    running_max = cum_ret.cummax()
    drawdown = (running_max - cum_ret) / running_max
    stats['max_drawdown'] = drawdown.max()
    stats['cum_ret_series'] = cum_ret
    stats['pnl_series'] = pnl.cumsum()
    return stats
