import feedparser
from config import RSS_FEEDS, MAX_ARTICLES

def collect_news():
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", "")[:300],
                "link": entry.get("link", "")
            })
            if len(articles) >= MAX_ARTICLES:
                break
    return articles