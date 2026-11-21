---
title: LangGraph Multi-Agent Financial Research System
date: "2026"
order: 1
summary: An autonomous multi-agent research pipeline using LangGraph, hybrid TF-IDF/vector RAG, and an iterative critic/revision loop.
status: Active Project
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/Multi-Agent-1)

## Overview

A multi-agent research system powered by **LangGraph** designed to automate equity and financial news research. The system coordinates specialized autonomous agents to gather market quotes, company overviews, SEC filings, financial news, and live web search data, synthesizes the findings through a hybrid semantic vector RAG engine, and generates a structured, cited research report through a bounded critic/revision feedback loop.

## Architecture & Workflow

```text
User Query
    ↓
Ticker Resolution & Query Cleaning (Offline mapping + Alpha Vantage fallback)
    ↓
Data Gathering Agents (Alpha Vantage, Finnhub, SEC EDGAR, Tavily)
    ↓
Hybrid Semantic Vector RAG Retrieval (TF-IDF sublinear embeddings + Cosine similarity)
    ↓
Draft Synthesis Agent
    ↓
Critic / Reflection Agent  ──[Revision Loop (Bounded)]──→ Draft Synthesis
    ↓ (Approved)
Final Cited Research Report
```

## Key Technical Highlights

- **Official LangGraph StateGraph Orchestration:** Utilizes `langgraph.graph.StateGraph` with state channel reducers (`Annotated[list, operator.add]`) and partial dictionary updates for reliable state management across agent turns.
- **Smart Tool API Caching:** Built a lightweight TTL caching layer (`tools/cache.py`) for external APIs (Alpha Vantage, Finnhub, SEC EDGAR, Tavily) to eliminate rate-limit quota exhaustion during multi-turn revision cycles.
- **Hybrid Semantic Vector RAG:** Engineered an in-memory hybrid retrieval engine utilizing Scikit-Learn sublinear TF-IDF vector embeddings with 1-2 n-grams and cosine similarity for high-precision semantic matching over financial context.
- **Robust Ticker Resolution:** Combines explicit symbol matching, possessive query normalization, an expanded offline corporate ticker map (Apple, Tesla, Costco, Nvidia, AMD, Intel, Disney), and automated Alpha Vantage search fallbacks.
- **Automated Test Suite:** Fully tested with `pytest` covering tool caching behavior, ticker resolution edge cases, LangGraph graph transitions, and critic routing boundaries.

## Tech Stack

- **Frameworks:** LangGraph, LangChain
- **Language:** Python 3.12
- **Vector & Embeddings:** Scikit-Learn (TF-IDF sublinear n-grams, cosine similarity)
- **External Data APIs:** Alpha Vantage, Finnhub, SEC EDGAR, Tavily Search API
- **Testing:** Pytest
