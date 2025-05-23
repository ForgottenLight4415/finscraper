from langchain_core.tools import Tool
from scraper_tool.fetcher import fetch_stock_data_yf

def get_stock_info_tool(ticker: str) -> str:
    data = fetch_stock_data_yf(ticker)
    return (
        f"Stock Price: {data['stock_price']}\n"
        f"EPS (TTM): {data['eps_ttm']}\n"
        f"PE Ratio: {data['pe_ratio']}\n"
        f"Market Cap: {data['market_cap']}\n"
        f"Revenue: {data['revenue']}\n"
        f"Net Income: {data['net_income']}"
    )

stock_data_tool = Tool(
    name="StockDataFetcher",
    func=get_stock_info_tool,
    description="Use this tool to fetch financial metrics of a public company by ticker symbol. Example: AAPL, MSFT, TSLA"
)