---
title: FinRAG — Financial Report Intelligence System
date: "2026"
order: 3
summary: Context-aware RAG pipeline for querying SEC filings, earnings releases, and annual reports using FAISS, LangChain, and Groq.
status: Active Project
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/FinRAG-boxbox)

## Overview

FinRAG is a specialized Retrieval-Augmented Generation (RAG) platform that empowers financial analysts and investors to upload complex financial documents (such as 10-K filings, quarterly earnings calls, and investor presentations) and query them with natural language to obtain grounded, context-aware answers.

## Architecture & Data Pipeline

```text
Financial PDF Reports (10-K, 10-Q, Earnings)
       ↓
Text & Table Extraction (PyMuPDF)
       ↓
Domain-Aware Chunking Strategy
       ↓
Dense Semantic Vector Embeddings (Sentence Transformers)
       ↓
FAISS Vector Store Indexing
       ↓
Retriever (Top-K Similarity Search)
       ↓
Prompt Augmentation & Context Grounding
       ↓
Groq Llama 3.1 Inference Engine
       ↓
Grounded Financial Insights & Citations
```

## Core Capabilities

- **Document Processing:** Efficient text and tabular extraction from multi-page financial statements using PyMuPDF.
- **Semantic Vector Storage:** High-speed vector similarity indexing with FAISS, paired with dense representations from Sentence Transformers.
- **Ultra-Fast LLM Inference:** Integrated with Groq's low-latency inference engine hosting Llama 3.1 to generate rapid, hallucination-resistant summaries.
- **Finance-Specific Prompt Engineering:** System prompts tailored to financial terminology, accounting disclosures, and risk factor extraction.
- **Interactive Web Interface:** Streamlit-powered application providing real-time document upload, progress indicators, and conversational exploration.

## Tech Stack

- **Language:** Python 3.10+
- **RAG & Orchestration:** LangChain
- **Vector Database:** FAISS
- **Embeddings:** Sentence Transformers
- **LLM Provider:** Groq (Llama 3.1)
- **PDF Extraction:** PyMuPDF
- **User Interface:** Streamlit
