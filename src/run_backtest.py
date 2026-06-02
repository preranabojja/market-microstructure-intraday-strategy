from src.data_loader import load_intraday_data
from src.feature_engineering import add_microstructure_features
from src.signal_generation import generate_signals
from src.backtester import backtest_strategy, compute_performance_metrics

def main():
    # 1. Load data
    df = load_intraday_data("/Users/prerana/Documents/market-microstructure-intraday-strategy/data/raw/spy_intraday.csv")

    # 2. Add features
    df_feat = add_microstructure_features(df)

    # 3. Generate signals
    df_sig = generate_signals(df_feat)

    # 4. Backtest
    df_bt = backtest_strategy(df_sig, trading_cost_bps=1.0)

    # 5. Compute metrics
    metrics = compute_performance_metrics(df_bt)

    print("Performance metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    # 6. Save results
    df_bt.to_csv("data/processed/spy_intraday_backtest_results.csv")

if __name__ == "__main__":
    main()