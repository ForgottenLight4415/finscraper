from typing import TypedDict, Optional

class StockData(TypedDict):
    stock_price: Optional[float]
    eps_ttm: Optional[float]
    pe_ratio: Optional[float]
    market_cap: Optional[float]
    revenue: Optional[float]
    net_income: Optional[float]