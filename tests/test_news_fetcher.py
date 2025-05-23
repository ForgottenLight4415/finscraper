from scraper_tool.news_fetcher import fetch_finance_news

def test_fetch_finance_news_basic():
    news = fetch_finance_news("AAPL", scrolls=1)  # Use 1 scroll for speed
    assert isinstance(news, list)
    assert len(news) > 0, "Expected at least one news article"

    for article in news:
        assert "title" in article
        assert "link" in article
        assert "summary" in article
        assert article["title"], "Title should not be empty"
        assert article["link"].startswith("https://finance.yahoo.com"), "Link should be a Yahoo URL"