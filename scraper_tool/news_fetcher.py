import time
from bs4 import BeautifulSoup
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_article_content(url: str) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)

    try:
        # Click the first "Story Continues" button only
        button = driver.find_element("css selector", "button.readmore-button")
        if button.is_displayed():
            button.click()
            time.sleep(1)  # Let expanded content load
    except Exception:
        pass  # No button found or click failed

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Get the first article only
    article_tag = soup.select_one("article div.body")
    if not article_tag:
        return "Main article not found"

    paragraphs = article_tag.select("p")
    content = " ".join(p.text.strip() for p in paragraphs if p.text.strip())
    return content or "Content not found"

def fetch_finance_news(ticker: str, scrolls: int = 5, limit: int = 3) -> List[Dict[str, str]]:
    url = f"https://finance.yahoo.com/quote/{ticker}/news"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    for _ in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()


    articles = []
    for item in soup.select("li.stream-item"):
        if item.select_one('a[href="/topic/premium-news/"]'):
            continue

        title_tag = item.select_one("h3")
        link_tag = item.select_one("a")
        summary_tag = item.select_one("p")

        if title_tag and link_tag:
            title = title_tag.text.strip()
            raw_href = link_tag.get("href", "")
            link = raw_href if raw_href.startswith("http") else "https://finance.yahoo.com" + raw_href
            summary = summary_tag.text.strip() if summary_tag else "No summary available"
            articles.append({"title": title, "link": link, "summary": summary})

        if len(articles) == limit:
            break

    for article in articles:
        article["content"] = extract_article_content(article["link"])

    return articles

import json
data = json.dumps(fetch_finance_news(ticker="AAPL", scrolls=1), indent=2)
print(data)