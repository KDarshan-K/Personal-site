---
title: ForexTrendML — USD/INR Macro-Quant Predictive System
date: "2026"
summary: Machine learning pipeline and interactive dashboard predicting 5-day directional USD/INR movements using XGBoost, FRED macro indicators, and financial backtesting.
status: Active Project
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/ForexTrendML-Boxbox)

## Overview

ForexTrendML is an end-to-end quantitative machine learning pipeline and interactive financial dashboard built to forecast the **5-day directional movement** of the USD/INR currency pair. By fusing technical price dynamics with macroeconomic data from the Federal Reserve Economic Data (FRED), the system provides probabilistic forecasts and backtested strategy evaluation for forex risk management.

## Key System Components

- **Automated Macro & Market Data Ingestion:** Seamless integration with Yahoo Finance for daily currency pricing and the FRED API for key macroeconomic signals (interest rate differentials, inflation, crude oil prices, dollar index).
- **Domain-Specific Feature Engineering:** Computes technical momentum indicators, moving average divergences, and rolling volatility metrics combined with lagged macroeconomic indicators.
- **Machine Learning Classification:** Trains and optimizes an **XGBoost Classifier** with strict time-series cross-validation to prevent forward-looking data leakage.
- **Backtesting Simulation Engine:** Implements a signal-based trading simulation with configurable confidence thresholds, reporting benchmark comparisons, total returns, and the Sharpe ratio.
- **Interactive Streamlit Web Dashboard:** Visualizes live inference, feature importance scores, historical trade performance, and price projection cones with confidence intervals.

## Tech Stack

- **Languages & Frameworks:** Python, XGBoost, Scikit-Learn, Pandas, NumPy
- **Financial & Macro APIs:** Yahoo Finance (`yfinance`), Federal Reserve Economic Data (`FRED API`)
- **Dashboard & Visualization:** Streamlit, Matplotlib, Seaborn, Plotly
