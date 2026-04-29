import json
import os
import time


def save_news(news_list):
    """
    Сохраняет каждую новость в отдельный файл.
    """
    os.makedirs("data", exist_ok=True)

    timestamp = int(time.time())

    for i, news in enumerate(news_list):
        filename = f"data/news_{timestamp}_{i}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(news, f, indent=2, ensure_ascii=False)
