import asyncio
import time

from crawler import crawl
from storage import save_news

INTERVAL = 30  # интервал в секундах


async def scheduler():
    """
    Запуск программы
    """
    while True:
        print("Старт краулинга")
        start = time.time()

        data = await crawl()

        save_news(data)

        duration = time.time() - start
        print(f"Готово за {duration:.2f} сек")

        print(f"Ожидание {INTERVAL} сек...\n")
        await asyncio.sleep(INTERVAL)


if __name__ == "__main__":
    asyncio.run(scheduler())