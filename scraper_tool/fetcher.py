import yfinance as yf
from .models import StockData
from .cache import default_cache
from curl_cffi.requests.exceptions import HTTPError

@default_cache()
def fetch_stock_data_yf(ticker: str) -> StockData:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info  # raises HTTPError for invalid tickers

        return StockData(
            stock_price=info.get("regularMarketPrice"),
            eps_ttm=info.get("trailingEps"),
            pe_ratio=info.get("trailingPE"),
            market_cap=info.get("marketCap"),
            revenue=info.get("totalRevenue"),
            net_income=info.get("netIncomeToCommon")
        )
    except HTTPError:
        return StockData(
            stock_price=None,
            eps_ttm=None,
            pe_ratio=None,
            market_cap=None,
            revenue=None,
            net_income=None
        )