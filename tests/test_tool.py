from scraper_tool.tool import get_stock_info_tool

def test_get_stock_info_tool_output():
    output = get_stock_info_tool("AAPL")
    assert isinstance(output, str)
    assert "Stock Price" in output
    assert "EPS (TTM)" in output
    assert "PE Ratio" in output
    assert "Market Cap" in output
    assert "Revenue" in output
    assert "Net Income" in output