---
title: Unified Logistics Hub
date: "2026"
order: 2
summary: AI-driven warehouse and logistics management platform featuring geospatial driver dispatch, HTMX tracking, and natural-language MongoDB querying via Groq.
status: Active Prototype
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/Unified-Logistics)

## Overview

Unified Logistics Hub is a full-stack logistics and warehouse management platform built with high performance, simplicity, and operational intelligence in mind. It provides end-to-end shipment lifecycle management, real-time driver allocation based on geospatial distance, and an intelligent AI admin query interface that translates natural language questions into executable database aggregations.

## Key Features

- **Shipment Lifecycle Tracking:** Full state-machine transitions across dispatch, transit, out-for-delivery, delivered, and returns with timestamped audit histories.
- **Geospatial Driver Assignment:** Leverages MongoDB's 2dsphere indexing and `$near` queries to match incoming dispatch requests to the closest available driver in sub-millisecond query time.
- **Real-Time Tracking without Client Bloat:** Replaces heavy single-page application frameworks with server-rendered Jinja2 templates and **HTMX** live status polling on shipment tracking views.
- **AI Admin Query Panel:** Operators can ask questions in plain English (e.g., *"Which warehouse had the highest return rate last week?"*). The system uses Groq (Llama 3.1 8B Instant) to synthesize and execute multi-stage MongoDB aggregation pipelines with strict schema boundaries.
- **Warehouse Analytics & Return Management:** Automated return rate computations, warehouse load balancing metrics, and driver utilization reporting.

## Tech Stack

- **Backend:** FastAPI, Python 3.12, Uvicorn
- **Database:** MongoDB (PyMongo) with 2dsphere geospatial indexing & aggregation pipelines
- **AI & LLM:** Groq API (Llama 3.1 8B Instant)
- **Frontend:** Jinja2, Tailwind CSS, HTMX
