# 📈 Stock Data Scraping Tool

A lightweight, caching-enabled Python submodule to fetch stock market data using `yfinance`. Designed for integration into larger systems, including LangChain agents.

---

## 🚀 Features

- Real-time financial data via `yfinance`
- Caching with `functools.lru_cache`
- Type-safe responses via `TypedDict`
- LangChain Tool support
- Unit-tested with `pytest`

---

## 🛠 Installation (as Git Submodule)

To add this submodule to another Git repository:

```bash
git submodule add https://github.com/your-username/scraper_tool.git scraper_tool
git submodule init
git submodule update