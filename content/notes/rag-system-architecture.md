---
title: Production RAG Architectures — Lessons in Retrieval and Grounding
date: "2026"
summary: Practical design considerations for domain-specific RAG systems, covering chunking topologies, hybrid retrieval, embedding selection, and latency optimization.
status: Engineering Note
---

Building a proof-of-concept RAG system takes ten lines of code; bringing it to production reliability requires solving data fragmentation, retrieval noise, and hallucination bounds.

---

## 1. Document Chunking: Beyond Naive Character Counts

Fixed-window chunking (e.g., 500 characters with 50-character overlap) frequently shears tables, cross-references, and code blocks in half.

- **Semantic & Header-Aware Chunking:** For markdown or HTML documents, split along document structural headers (`H1`, `H2`, `H3`) to preserve natural semantic scoping.
- **Parent-Child Chunking:** Index small chunks (e.g., 200 tokens) for high-precision semantic similarity retrieval, but pass the broader parent section (e.g., 1000 tokens) to the LLM context window to prevent loss of local nuance.
- **Tabular Data Treatment:** In financial and technical documents, convert tables into markdown or key-value representations before embedding, or isolate them into dedicated structured SQL / Pandas lookup agents.

---

## 2. Hybrid Retrieval: Dense + Sparse Fusion

Dense vector search (embeddings) understands conceptual semantics, but struggles with exact alphanumeric tokens—like ticker symbols (`AAPL`, `GOOGL`), part IDs, or exact error codes.

- **Sparse Search (BM25 / TF-IDF):** Unbeatable for exact keyword and token matches.
- **Dense Search (Cosine Similarity over Embeddings):** Captures synonyms, conceptual paraphrasing, and thematic relevance.
- **Reciprocal Rank Fusion (RRF):** Combine rankings from both sparse and dense retrievers:
  $$RRF\_Score(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
  where $r_m(d)$ is the rank of document $d$ in system $m$, and $k$ is a smoothing constant (typically $60$).

---

## 3. Re-ranking: The Quality Filter

A vector index typically returns the top-$K$ candidates (e.g., $K=25$), but feeding all 25 documents into an LLM degrades context attention ("lost in the middle" phenomenon) and inflates token cost.

- Deploy a lightweight Cross-Encoder re-ranker (such as `bge-reranker`) over the retrieved candidates.
- Cross-encoders perform joint attention between the query and candidate passage, filtering down to the top 3-5 most pertinent context chunks for generation.

---

## 4. Latency & Caching Bottlenecks

- **Prompt Caching:** Utilize provider prompt caching (or KV cache persistence) for static system prompts and pinned reference documents.
- **TTL Cache on Retrieval:** Many user queries in financial and operational domains query identical entities repeatedly. Caching vector retrieval results by hash of normalized query dramatically reduces database load and API costs.
