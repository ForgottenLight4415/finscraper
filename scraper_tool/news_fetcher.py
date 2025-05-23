import time
from bs4 import BeautifulSoup
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_finance_news(ticker: str, scrolls: int = 5) -> List[Dict[str, str]]:
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
            link = "https://finance.yahoo.com" + link_tag.get("href", "")
            summary = summary_tag.text.strip() if summary_tag else "No summary available"
            articles.append({"title": title, "link": link, "summary": summary})

    return articles
