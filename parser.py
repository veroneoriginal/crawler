from bs4 import BeautifulSoup

BASE_URL = "https://news.ycombinator.com/"


# Парсинг списка новостей с главной страницы
def parse_news(html: str):
    soup = BeautifulSoup(html, "html.parser")
    items = []

    rows = soup.select(".athing")

    for row in rows:
        title_tag = row.select_one(".titleline a")
        if not title_tag:
            continue

        title = title_tag.text
        link = title_tag.get("href")

        subtext = row.find_next_sibling("tr")
        comments_tag = subtext.select_one("a[href*='item?id=']")

        comments_link = None
        if comments_tag:
            comments_link = BASE_URL + comments_tag.get("href")

        items.append({
            "title": title,
            "link": link,
            "comments_link": comments_link
        })

    return items


# Парсинг ссылок из комментариев
def parse_comment_links(html: str):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.select(".comment a"):
        href = a.get("href")
        if href and href.startswith("http"):
            links.add(href)

    return list(links)