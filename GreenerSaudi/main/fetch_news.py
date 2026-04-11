import feedparser

url = "https://news.google.com/rss/search?q=Saudi+Arabia+green+initiative&hl=en-US&gl=US&ceid=US:en"
feed = feedparser.parse(url)

def fetch_latest_news():
    news = []

    for entry in feed.entries[:10]:
        title = entry.title.strip()
        link = entry.link.strip()
        date = entry.published.strip()
        publisher = entry.source.title.strip() if 'source' in entry else 'Unknown'
        print("TITLE:", title)
        print("DATE:", date)
        print("LINK:", link)
        print("PUBLISHER:", publisher)
        news.append({
            "title": title,
            "link": link,
            "date": date,
            "publisher": publisher,
        })
        print("-" * 60)
    return news

fetch_latest_news()