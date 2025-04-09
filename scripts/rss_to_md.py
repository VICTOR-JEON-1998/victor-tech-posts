import feedparser
from datetime import datetime, timedelta
import os
import re

# Tistory RSS 주소
RSS_URL = "https://jeon-maker.tistory.com/rss"
feed = feedparser.parse(RSS_URL)

# 오늘 날짜 기준 계산
today = datetime.today()
cutoff = today - timedelta(days=1)  # 최근 1일 이내

# 글 파싱
for entry in feed.entries:
    title = entry.title
    content = entry.summary
    published = entry.published_parsed
    date_obj = datetime(*published[:6])
    date_str = date_obj.strftime('%Y-%m-%d')
    year = date_obj.strftime('%Y')
    month = date_obj.strftime('%m')

    # ✅ 최근 하루 이내 글만 수집
    if date_obj < cutoff:
        continue

    # ✅ slug 생성 + 날짜 접미어 추가
    base_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    slug = f"{date_str}-{base_slug}"

    # ✅ 폴더 경로 생성
    folder_path = f"posts/{year}/{month}"
    os.makedirs(folder_path, exist_ok=True)
    filename = f"{folder_path}/{slug}.md"

    # ✅ 중복 방지
    if os.path.exists(filename):
        continue

    # ✅ 파일 작성
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"**Posted on**: {date_str}\n\n")
        f.write(content)

print("✅ Tistory RSS Sync Complete (오늘 글만)")
