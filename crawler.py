import aiohttp
import asyncio
from parser import parse_news, parse_comment_links


async def fetch(session, url: str):
    """ Загрузка страницы """
    async with session.get(url) as response:
        return await response.text()



async def process_news(session, news: dict):
    """
    Обработка одной новости
    (добавление ссылки из комментариев)
    """
    if not news["comments_link"]:
        news["comment_links"] = []
        return news

    try:
        html = await fetch(session, news["comments_link"])
        news["comment_links"] = parse_comment_links(html)
    except Exception:
        news["comment_links"] = []

    return news



async def crawl():
    """
    Основной краулинг
    """
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://news.ycombinator.com/")
        news_list = parse_news(html)

        tasks = [process_news(session, n) for n in news_list]
        result = await asyncio.gather(*tasks)

        return result