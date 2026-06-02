# 📈 Market Microstructure Intraday Strategy  
*A research‑grade intraday trading engine built with Python, microstructure features, and a modular backtesting pipeline.*

---

## 🚀 Overview  
This project implements a complete intraday trading research workflow used in real quant environments:

- High‑frequency **microstructure feature engineering**
- Systematic **signal generation**
- Vectorized **backtesting engine**
- Robust **performance and risk metrics**
- Clean, modular **Python architecture**
- Reproducible **Jupyter research notebooks**

It demonstrates the full lifecycle of a quant research project — from raw data to deployable strategy logic — in a transparent, extensible, and production‑aligned way.

---

## Business Problem 
Intraday markets generate massive volumes of high‑frequency data, but most trading signals fail to capture the microstructure dynamics that drive short‑horizon price movements. Traditional daily‑bar strategies overlook critical information such as volatility bursts, liquidity shifts, order‑flow imbalance, and volume anomalies — all of which influence execution quality, short‑term returns, and risk.

For trading desks, the challenge is twofold:

1. **Identify microstructure‑driven patterns** that are stable, interpretable, and predictive at intraday horizons.
2. **Convert these patterns into actionable signals** that can be backtested, stress‑tested, and deployed within a systematic trading framework.

This project addresses that challenge by building a complete research pipeline that:

- Processes raw intraday data into clean, analysis‑ready time series  
- Engineers microstructure features that capture short‑term market behavior  
- Generates interpretable trading signals grounded in market intuition  
- Backtests the strategy against a buy‑and‑hold benchmark  
- Evaluates performance using institutional‑grade risk metrics  

The goal is to demonstrate how microstructure‑aware signals can improve intraday decision‑making, enhance execution timing, and provide a measurable edge over naive strategies — a capability directly relevant to quantitative trading, electronic market‑making, and execution‑focused roles across major banks and hedge funds.

## 🔍 Microstructure Features  
The strategy uses several high‑signal microstructure features:

- Short‑horizon **momentum**
- Rolling **volatility**
- **Volume Z‑score** anomalies
- Intraday **volatility bursts**

These features are engineered in `src/feature_engineering.py` and explored in Notebook 02.

---

## 📡 Signal Generation  
Signals are generated using interpretable, production‑aligned rules:

- Momentum > threshold → **long**
- Momentum < −threshold → **short**
- Volatility spikes → **risk‑off**
- Volume anomalies → **noise filter**

This ensures the strategy is:

- Transparent  
- Explainable  
- Easy to debug  
- Easy to extend into ML‑based signals  

---

## 📊 Backtesting Engine  
The backtester computes:

- Strategy returns  
- Buy‑and‑hold benchmark  
- Cumulative returns  
- Drawdowns  
- Trade count  
- Sharpe ratio  
- Max drawdown  
- Volatility  

The engine is vectorized and modular, allowing easy extension to:

- Transaction costs  
- Slippage  
- Multi‑asset portfolios  
- Parameter sweeps  

---

## 📈 Visualizations  
Notebook 04 generates:

- **Equity curve** (strategy vs. buy‑and‑hold)  
- **Drawdown curve**  
- **Signal overlays**  
- **Feature distributions**  

These plots demonstrate the strategy’s behavior and robustness.

---

## 🧪 Reproducible Research Workflow  
Each notebook corresponds to a stage in the quant research lifecycle:

1. **01_exploration** — Inspect raw intraday data  
2. **02_feature_engineering** — Build microstructure features  
3. **03_signal_and_backtest** — Generate signals + run backtest  
4. **04_visualizations** — Plot equity curve + drawdown  

This mirrors the workflow used by quant researchers and strat teams.

---

## ⚙️ Installation  
```bash
git clone https://github.com/preranabojja/market-microstructure-intraday-strategy.git
cd market-microstructure-intraday-strategy
pip install -r requirements.txt
```

## 📁 Data
Raw and processed data are not included in the repository for size and compliance reasons.

To run the pipeline:
- Place your intraday CSV in data/raw/
- Ensure it contains columns:
- date, open, high, low, close, volume, barCount
- Run the notebooks or the backtest script

## 🧩 Extensions (Future Work)
This project is designed to be extended. 
Potential additions include:
- Machine learning signals (Random Forest, XGBoost, LSTM)
- Regime detection
- Transaction cost modeling
- Multi‑ticker backtesting
- Parameter optimization
- Execution‑aware microstructure models

