---
title: Adversarial CAPTCHA Recognition & Robustness
date: "2026"
summary: PyTorch CNN sequence recognition model evaluated against FGSM and PGD adversarial perturbations, incorporating adversarial defense training.
status: Experiment & Defense Study
---

[View Repository on GitHub ↗](https://github.com/KDarshan-K/Adversial-Captcha-Breaking-System-)

## Overview

A computer vision and deep learning study investigating the vulnerability and defensive robustness of visual sequence recognition systems under adversarial attack conditions. The system recognizes 5-character alphanumeric CAPTCHAs and systematically evaluates model degradation under gradient-based adversarial perturbations.

## Pipeline & Architecture

- **Data Preprocessing & Augmentation:** Image ingestion pipeline converting multi-channel CAPTCHA images into normalized grayscale tensors with noise injection, shearing, and rotation augmentations.
- **Deep Convolutional Architecture:** Built with PyTorch, utilizing stacked convolutional blocks with batch normalization, max-pooling, and multi-head classification layers predicting individual characters simultaneously.
- **Adversarial Attack Simulation:** Implemented white-box adversarial attacks including:
  - **Fast Gradient Sign Method (FGSM):** One-step gradient perturbation testing susceptibility to $L_\infty$-bounded noise.
  - **Projected Gradient Descent (PGD):** Iterative multi-step adversarial perturbation uncovering worst-case failure modes.
- **Adversarial Training Defense:** Retrained the network on perturbed gradient examples, significantly mitigating accuracy drops under attack without sacrificing clean image recognition accuracy.
- **Visualization Tooling:** Scripts to generate side-by-side perturbation heatmaps, confidence degradation curves, and prediction breakdowns.

## Tech Stack

- **Framework:** PyTorch, Torchvision
- **Language:** Python 3.10+
- **Image Processing:** OpenCV, Pillow, NumPy
- **Adversarial Methods:** FGSM, PGD, Adversarial Defense Training
