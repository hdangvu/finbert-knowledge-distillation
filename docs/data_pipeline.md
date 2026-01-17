# Data Pipeline: News Ingestion → Storage → Cleaning

This project includes a lightweight data engineering pipeline to collect and prepare
financial news text for downstream sentiment modeling.

## 1) Ingestion (Bronze Layer)
**Script:** `scripts/ingest/scrape_news.py`

- Iterates over a predefined universe of equity tickers (e.g., NVDA, AMD, AAPL)
- Fetches paginated news listing pages and parses article metadata:
  - `datetime`, `symbol`, `source`, `title`, `link`
- Applies basic rate limiting to reduce request bursts
- Writes raw output to: `data/raw/scraped_data.csv` (excluded from git)

## 2) Storage Layout
- `data/raw/` — raw scraped output (local only; not tracked)
- `data/processed/` — cleaned/model-ready data (local only; not tracked)
- `data/sample/` — safe public sample (tracked), containing metadata + derived stats
  (no full article text redistributed)

## 3) Cleaning / Text Preparation (Silver Layer)
Cleaning steps (implemented in the notebook and can be modularized):
- lowercasing
- whitespace normalization
- ASCII normalization (remove problematic unicode)
- concatenate `title_clean + summary_clean` into `text_clean` for modeling

## 4) Data Quality Notes
Recommended checks (and easy extensions):
- drop rows with missing `link` or invalid timestamps
- de-duplicate by `link` (or hash of link)
- log counts per ticker and per source
- track null rate for `summary`

## 5) Reproducibility & Compliance
The repository does not redistribute the full scraped dataset publicly.
It provides ingestion code, schema documentation, and a small metadata-only sample
in `data/sample/` for demonstration.