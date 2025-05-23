from scraper_tool.fetcher import fetch_stock_data_yf

def test_fetch_valid_ticker():
    result = fetch_stock_data_yf("AAPL")
    assert isinstance(result, dict)
    assert "stock_price" in result
    assert isinstance(result["stock_price"], (float, type(None)))

def test_fetch_invalid_ticker():
    result = fetch_stock_data_yf("INVALIDTICKER")
    assert all(val is None or isinstance(val, float) for val in result.values())