---
title: C++ Containers — Practical Notes
date: "Draft"
summary: When to use vector, map, unordered_map, set, priority_queue, and other standard containers.
---
## Choose based on operations

- Use `vector` for contiguous storage and fast indexed access.
- Use `unordered_map` for average constant-time key lookup when ordering is unnecessary.
- Use `map` when sorted keys and logarithmic operations matter.
- Use `priority_queue` when repeatedly retrieving the highest- or lowest-priority element.

Always account for memory, ordering requirements, and worst-case behavior.
