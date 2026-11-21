---
title: System Design — Fundamental Patterns and Trade-offs
date: "2026"
summary: Practical architectural patterns on caching topologies, database sharding, asynchronous event queues, and distributed consensus trade-offs.
status: Engineering Note
---

Engineering scalable systems is not about adopting buzzwords; it is about choosing the least bad set of trade-offs for a concrete set of constraints.

---

## 1. Requirement Scoping & Capacity Estimation

Before drawing boxes, delineate the operational boundaries:

1. **Functional vs Non-Functional Requirements:**
   - Functional: Core API contracts and data mutations.
   - Non-Functional: Latency SLA ($p95 < 50\text{ms}, p99 < 150\text{ms}$), throughput (QPS read vs write ratio), availability ($99.9\%$ vs $99.99\%$), and consistency requirements.
2. **Back-of-the-Envelope Estimation:**
   - Read vs Write Heavy: A $100:1$ read-to-write ratio dictates heavy caching layers; a $1:1$ ratio necessitates append-only log-structured stores (LSM trees).
   - Storage Growth: $\text{Daily Writes} \times \text{Avg Payload Size} \times 365 \times \text{Retention Years} \times \text{Replication Factor}$.

---

## 2. Caching Topologies & Invalidation

Caches bridge the microsecond memory gap against the millisecond disk/network boundary.

| Strategy | Read Path | Write Path | Invalidation / Consistency | Best For |
|---|---|---|---|---|
| **Cache-Aside (Lazy Loading)** | App queries cache; on miss, queries DB and populates cache | App writes directly to DB, invalidates cache key | Eventual consistency; risk of stale reads during high concurrency | Read-heavy workloads with irregular access patterns |
| **Read-Through / Write-Through** | App reads from cache; cache fetches from DB | App writes to cache; cache synchronously writes to DB | High consistency; write latency is bounded by slowest store | Financial data, inventory where stale reads are unacceptable |
| **Write-Behind (Write-Back)** | App reads from cache | App writes to cache; cache asynchronously batches writes to DB | Eventual consistency; risk of data loss if cache crashes before flush | High-throughput write surges (e.g., telemetry, clickstreams) |

---

## 3. Database Scaling: Replication vs Partitioning

- **Read Replicas:** Great for scaling reads. Bottlenecks emerge around replication lag (causing read-your-own-writes anomalies). Mitigate by routing user-specific immediate reads to the primary database.
- **Horizontal Sharding:**
  - **Range-Based:** Keys partitioned by alphabetical or timestamp ranges. Vulnerable to hot-spotting (e.g., all new records write to the same recent partition).
  - **Hash-Based:** $\text{hash}(key) \pmod N$. Distributes load evenly, but adding/removing a shard invalidates almost all key locations.
  - **Consistent Hashing:** Arranges nodes on a virtual hash ring with virtual nodes to balance distribution and minimize data migration when nodes fail or scale out.

---

## 4. Decoupling with Asynchronous Messaging

Direct synchronous HTTP/gRPC calls between services introduce tight coupling and cascading failure modes.

- **Message Queues (RabbitMQ, SQS):** Transient point-to-point worker task dispatching. Excellent for background job offloading.
- **Distributed Event Logs (Apache Kafka):** Append-only persistent commit log. Multiple independent consumer groups replay events at their own pace.
- **Delivery Guarantees:**
  - *At-most-once:* Fire and forget; loss tolerated.
  - *At-least-once:* Standard; duplicates possible; consumers **must be idempotent** (using deduplication keys / unique constraints).
  - *Exactly-once:* High coordination overhead; requires distributed transactions or two-phase commits.

---

## 5. The Distributed Reality: PACELC

While the CAP theorem states you must choose Consistency or Availability under Partitioning (**P**), Daniel Abadi's **PACELC** theorem captures normal operation:

> If there is a Partition (**P**), how does the system trade off Availability (**A**) vs Consistency (**C**);  
> **Else** (**E**), how does the system trade off Latency (**L**) vs Consistency (**C**)?

- **DynamoDB / Cassandra:** PA/EL (prioritize availability during partitions; minimize latency in normal operations).
- **Postgres / Spanner:** PC/EC (prioritize strict serializable consistency at the expense of latency and availability during partitions).
