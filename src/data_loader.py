import pandas as pd

def load_intraday_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Rename date column to timestamp
    df = df.rename(columns={'date': 'timestamp'})

    # Convert to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Sort and index
    df = df.sort_values('timestamp')
    df = df.set_index('timestamp')

    # Keep only regular trading hours (optional but recommended)
    df = df.between_time('09:30', '16:00')

    return df