from scraper_tool.news_fetcher import fetch_finance_news

def test_fetch_finance_news_basic():
    news = fetch_finance_news("AAPL", scrolls=1, limit=2)
    assert isinstance(news, list), "Expected a list of articles"
    assert len(news) > 0, "Expected at least one news article"

    for article in news:
        assert isinstance(article, dict), "Each article should be a dictionary"
        assert "title" in article and article["title"], "Article title missing or empty"
        assert "link" in article and article["link"].startswith("https://finance.yahoo.com"), "Invalid article link"
        assert "summary" in article, "Article summary missing"
        assert "content" in article, "Content field missing after threading"
        assert isinstance(article["content"], str), "Content should be a string"
        assert article["content"] != "Content not found", "Content was not extracted properly"