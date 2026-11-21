---
title: C++ Containers — Practical Engineering Notes
date: "2026"
summary: A practical guide on STL container selection, memory layouts, cache locality, iterator invalidation, and common performance pitfalls.
status: Engineering Note
---

Choosing the right container in modern C++ (C++17 / C++20) is fundamentally an exercise in understanding **memory locality**, **allocation overhead**, and **algorithmic complexity**.

---

## 1. Quick Decision Matrix

| Container | Underlying Storage | Lookup Complexity | Insertion / Deletion | Best For |
|---|---|---|---|---|
| `std::vector` | Contiguous dynamic array | $O(1)$ random access | $O(1)$ amortized at back; $O(N)$ elsewhere | Default choice for almost all sequences |
| `std::deque` | Chunks of contiguous arrays | $O(1)$ random access | $O(1)$ at both front and back | Queue-like buffers with double-ended growth |
| `std::list` | Doubly-linked list | $O(N)$ sequential | $O(1)$ if iterator is known | Frequent splicing or stable iterators needed |
| `std::unordered_map` | Hash table (separate chaining) | $O(1)$ average; $O(N)$ worst | $O(1)$ average; $O(N)$ worst | High-volume key lookup without ordering |
| `std::map` | Red-Black Tree (Balanced BST) | $O(\log N)$ | $O(\log N)$ | Keys must stay sorted or range queries needed |
| `std::priority_queue` | Binary heap (vector-backed) | $O(1)$ `top()` | $O(\log N)$ `push()` / `pop()` | Streaming top-K or Dijkstra / shortest path |

---

## 2. Why `std::vector` Dominates: Cache Locality

Theoretical Big-O analysis often hides CPU hardware realities. A linked list (`std::list`) provides $O(1)$ insertion anywhere given a pointer, yet `std::vector` typically outperforms it even for insertions in the middle for modest sizes:

- **L1/L2 Cache Prefetching:** CPU hardware prefetchers load contiguous cache lines (typically 64 bytes). Iterating over a `vector` minimizes cache misses.
- **Node Overhead:** Node-based structures (`std::list`, `std::map`) incur pointer overhead (16-24 bytes per node on 64-bit platforms) plus heap fragmentation.
- **Tip:** Always call `vec.reserve(expected_size)` prior to insertion loops to avoid reallocation copies.

---

## 3. `std::map` vs `std::unordered_map` Trade-offs

- **Hashing Overhead:** `std::unordered_map` requires calculating a hash. For small keys (e.g., integers), this is trivial, but for long strings, hashing can cost more than tree traversal.
- **Worst-Case Guarantees:** `std::map` guarantees $O(\log N)$ worst-case time, essential for hard real-time systems where hash collisions can degrade `unordered_map` to $O(N)$.
- **Range Queries:** If you need `lower_bound`, `upper_bound`, or sorted iteration, `std::map` is mandatory.

---

## 4. Iterator Invalidation Rules

A frequent source of memory corruption and undefined behavior:

- **`std::vector`:**
  - `push_back()` / `emplace_back()`: Invalidates **all** iterators if `capacity()` was exceeded (reallocation). If no reallocation, only `end()` is invalidated.
  - `erase()`: Invalidates iterators at or after the point of erasure.
- **`std::deque`:**
  - Inserting at either end invalidates iterators, but references to elements remain valid.
- **`std::unordered_map` & `std::map`:**
  - Node-based: Iterators and references to other elements remain valid when inserting or deleting elements (except the deleted element's iterator).
