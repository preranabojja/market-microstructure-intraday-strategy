import pandas as pd
import numpy as np

def add_microstructure_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Simple returns
    df['return'] = df['close'].pct_change()

    # 2. Rolling volatility (e.g., last 15 bars)
    window_vol = 15
    df['rolling_vol'] = df['return'].rolling(window_vol).std()

    # 3. Rolling average volume and volume z-score
    window_volu = 30
    df['avg_volume'] = df['volume'].rolling(window_volu).mean()
    df['volume_zscore'] = (df['volume'] - df['avg_volume']) / df['avg_volume'].replace(0, np.nan)

    # 4. Short-term momentum: return over last N bars
    window_mom = 10
    df['momentum'] = df['close'].pct_change(window_mom)

    # Drop initial NaNs
    df = df.dropna()

    return df