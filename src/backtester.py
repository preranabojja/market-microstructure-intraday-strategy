import pandas as pd
import numpy as np

def backtest_strategy(df: pd.DataFrame,
                      trading_cost_bps: float = 1.0) -> pd.DataFrame:
    """
    df must contain: 'close', 'signal'
    trading_cost_bps: cost per trade in basis points (e.g., 1.0 = 0.01%)
    """
    df = df.copy()

    # Compute returns
    df['return'] = df['close'].pct_change().fillna(0)

    # Position is previous signal (enter at next bar)
    df['position'] = df['signal'].shift(0).fillna(0)

    # Strategy gross return
    df['strategy_return_gross'] = df['position'] * df['return']

    # Trading cost when position changes
    df['trade'] = df['position'].diff().abs().fillna(0)
    cost_per_trade = trading_cost_bps / 10000.0  # bps to decimal
    df['trading_cost'] = df['trade'] * cost_per_trade

    # Net strategy return
    df['strategy_return_net'] = df['strategy_return_gross'] - df['trading_cost']

    # Cumulative returns
    df['cum_return_strategy'] = (1 + df['strategy_return_net']).cumprod()
    df['cum_return_buy_hold'] = (1 + df['return']).cumprod()

    return df

def compute_performance_metrics(df: pd.DataFrame) -> dict:
    """
    df must contain 'strategy_return_net' and 'return'
    """
    strat_ret = df['strategy_return_net']
    buy_hold_ret = df['return']

    # Annualization factor (approx): assume 252 trading days * ~390 minutes per day / bar_interval
    # For 1-min bars: 252 * 390 ≈ 98280
    # For simplicity, we can use 252 for daily-like scaling or leave as is and call it "per-bar Sharpe".
    ann_factor = 252

    strat_mean = strat_ret.mean()
    strat_std = strat_ret.std()

    sharpe = (strat_mean / strat_std) * np.sqrt(ann_factor) if strat_std != 0 else 0

    # Max drawdown
    cum = (1 + strat_ret).cumprod()
    peak = cum.cummax()
    drawdown = (cum - peak) / peak
    max_dd = drawdown.min()

    metrics = {
        "strategy_total_return": cum.iloc[-1] - 1,
        "buy_hold_total_return": (1 + buy_hold_ret).cumprod().iloc[-1] - 1,
        "sharpe_ratio": sharpe,
        "max_drawdown": max_dd,
        "num_trades": df['trade'].sum()
    }

    return metrics