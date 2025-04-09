import feedparser
from datetime import datetime
import os
import re

RSS_URL = "https://jeon-maker.tistory.com/rss"  # 블로그 주소로 바꾸기

feed = feedparser.parse(RSS_URL)

if not os.path.exists("2025/04"):
    os.makedirs("2025/04")

for entry in feed.entries[:3]:
    title = entry.title
    content = entry.summary
    date = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d')
    filename = f"2025/04/{re.sub(r'[^a-z0-9]+', '-', title.lower())}.md"

    if os.path.exists(filename):
        continue

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"**Posted on**: {date}\n\n")
        f.write(content)

print("✅ Tistory RSS Sync Complete")

