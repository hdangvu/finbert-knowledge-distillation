# Efficient Financial Sentiment Modeling via Knowledge Distillation

This repository contains experiments on distilling **FinBERT** into a compact
**ALBERT** student model for efficient financial sentiment classification.

## Overview
- Teacher: ProsusAI/finbert
- Student: albert-base-v2
- Methods: CE, Knowledge Distillation (KD), Patient Knowledge Distillation (PKD)
- Datasets:
  - Pseudo-labeled scraped financial news
  - Financial PhraseBank (100% agreement)

## Results (Financial PhraseBank)
The following confusion matrix compares four models:
- Fresh ALBERT
- CE-scraped → FP
- KD-scraped (T=5) → FP
- PKD-scraped → FP

![Confusion Matrix](assets/confusion_matrix_phrasebank.png)

## Repository structure
- `notebooks/`: Original Colab notebook containing all experiments
- `assets/`: Figures used in analysis

## Note
Experiments were conducted in Google Colab. This repository archives
final results and provides code structure for reproducibility.
