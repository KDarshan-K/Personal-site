---
title: Telco Customer Churn Prediction Pipeline
date: "2026"
summary: End-to-end customer churn classification engine with custom feature engineering, hyperparameter-tuned Random Forest, and a real-time Streamlit app.
status: Active Project
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/Teleco-Churn-boxbox-)

## Overview

An end-to-end machine learning engineering project designed to identify telecommunications customers at high risk of churning before contract termination. Built with a production-style workflow spanning raw data cleaning, domain-driven feature derivation, model training via hyperparameter search, and a decision-support dashboard for business stakeholders.

## Technical Details

- **Domain-Specific Feature Engineering:** Engineered high-signal behavioral features including:
  - `Tenure_Group`: Categorized customer lifecycle phases.
  - `TotalAddon_Count`: Composite measure of auxiliary service adoption (device protection, tech support, streaming).
  - `Monthly_vs_Average_Diff`: Identifying sudden pricing anomalies or bill-shock tendencies.
  - `Customer_Value_Tier`: Segmenting churn likelihood against lifetime revenue.
- **Model Training & Optimization:** Trained and tuned a **Random Forest Classifier** using `RandomizedSearchCV` with 5-fold cross-validation, optimizing for recall on the churn positive class to minimize business revenue loss.
- **Interactive Inference App:** Implemented a Streamlit web interface providing dynamic customer profile inputs, live risk categorization (Low, Medium, High), and feature importance breakdowns to assist customer retention agents.

## Tech Stack

- **Machine Learning:** Scikit-Learn (Random Forest, RandomizedSearchCV), Pandas, NumPy
- **Application & UI:** Streamlit
- **Visualization:** Matplotlib, Seaborn
