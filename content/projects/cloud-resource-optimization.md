---
title: Secure Cloud Resource Optimization with Reinforcement Learning
date: "In progress"
summary: Research prototype investigating adaptive reinforcement learning algorithms for cloud virtual machine allocation, energy conservation, SLA guarantees, and security constraints.
status: Research Prototype
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/Secure-AI-Cloud-Resource-Optimization-using-RL)

## Overview

Modern cloud data centers struggle with static or rule-based virtual machine (VM) scheduling, frequently resulting in idle power draw, severe over-provisioning costs, or SLA violations during demand surges. This research prototype explores formulating cloud workload consolidation and server power-state management as a **Reinforcement Learning (RL)** problem under multi-objective constraints.

## Problem Formulation & Methodology

- **State Space:** Captures server CPU utilization, memory pressure, active VM counts, bandwidth saturation, and tenant security isolation levels.
- **Action Space:** Discrete actions mapping VM migrations, server wake-up/sleep commands, and resource throttling.
- **Multi-Objective Reward Function:**
  $$R_t = -\alpha \cdot \text{Energy}(t) - \beta \cdot \text{SLAViolations}(t) - \gamma \cdot \text{MigrationCost}(t) - \delta \cdot \text{SecurityPenalty}(t)$$
  Balancing operational energy savings against stringent quality-of-service guarantees and tenant security colocation constraints.
- **Simulation Environment:** Emulates heterogeneous cloud workloads and host servers to evaluate agent policies against classical heuristic schedulers (First-Fit Decreasing, Best-Fit).

## Tech Stack & Tools

- **Frameworks:** Python, PyTorch / Stable-Baselines3, Gym/Gymnasium
- **Optimization:** Reinforcement Learning (PPO / DQN), Heuristic Baselines
- **Status:** Ongoing research investigation and empirical benchmarking
