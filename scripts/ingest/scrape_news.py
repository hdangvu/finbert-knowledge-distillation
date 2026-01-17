"""
News ingestion script.

Scrapes financial news articles for a predefined universe of equity tickers,
parses article metadata, and stores raw results locally.

Note:
- This script is provided for demonstration and reproducibility.
- Scraped content is not redistributed in this repository.
"""

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


SYMBOLS = [
    "nvda", "amd", "avgo", "intc", "qcom", "mu", "tsm", "asml", "arm", "smci",
    "aapl", "msft", "googl", "meta", "amzn", "crm", "orcl", "ibm", "adbe", "sap",
    "jpm", "bac", "c", "gs", "ms", "wfc", "schw", "axp", "pypl", "v",
    "wmt", "cost", "hd", "sbux", "tgt", "nke", "mcd", "dis", "tsla", "rivn",
    "xom", "cvx", "lmt", "ba", "cat", "gm", "f", "ge", "noc", "de"
]


def scrape_symbol(symbol: str, max_pages: int = 20) -> list[dict]:
    rows = []
    session = requests.Session()

    for page in range(1, max_pages + 1):
        url = f"https://markets.businessinsider.com/news/{symbol}-stock?p={page}"
        resp = session.get(url, timeout=10)
        if resp.status_code != 200:
            continue

        soup = BeautifulSoup(resp.text, "lxml")
        articles = soup.find_all("div", class_="latest-news__story")

        for article in articles:
            try:
                dt = article.find("time", class_="latest-news__date").get("datetime")
                title = article.find("a", class_="news-link").get_text(strip=True)
                source = article.find("span", class_="latest-news__source").get_text(strip=True)
                link = article.find("a", class_="news-link").get("href")
            except AttributeError:
                continue

            if link and link.startswith("/"):
                link = "https://markets.businessinsider.com" + link

            rows.append({
                "datetime": dt,
                "symbol": symbol,
                "source": source,
                "title": title,
                "link": link,
            })

        time.sleep(1.0)  # basic rate limiting

    return rows


def main():
    all_rows = []

    for symbol in SYMBOLS:
        print(f"Scraping {symbol}")
        rows = scrape_symbol(symbol)
        all_rows.extend(rows)

    df = pd.DataFrame(all_rows)
    print(f"Collected {len(df)} records")

    # NOTE: actual storage location is excluded from git
    df.to_csv("data/raw/scraped_data.csv", index=False)


if __name__ == "__main__":
    main()