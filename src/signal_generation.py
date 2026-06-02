import pandas as pd

def generate_signals(df: pd.DataFrame,
                     mom_threshold: float = 0.001,
                     vol_threshold: float = 0.005,
                     vol_zscore_threshold: float = 0.0) -> pd.DataFrame:
    """
    df must contain: 'momentum', 'rolling_vol', 'volume_zscore'
    """
    df = df.copy()

    # Initialize signal column
    df['signal'] = 0

    # Long when:
    # - momentum positive and above threshold
    # - volatility not too high
    # - volume at or above average (z-score >= threshold)
    long_condition = (
        (df['momentum'] > mom_threshold) &
        (df['rolling_vol'] < vol_threshold) &
        (df['volume_zscore'] >= vol_zscore_threshold)
    )

    df.loc[long_condition, 'signal'] = 1

    # short_condition = (df['momentum'] < -mom_threshold)
    # df.loc[short_condition, 'signal'] = -1

    # Shift signal by 1 bar to avoid look-ahead bias
    df['signal'] = df['signal'].shift(1).fillna(0)

    return df