import asyncio
import aiohttp


urls = [
    'https://habr.com/ru',
    'https://rozetka.com.ua/ua/',
    'https://www.python.org/',
    'https://www.netflix.com/browse'
]


async def async_url(url):
    async with aiohttp.request('get', url) as request:
        print(request.status)
        return url


async def async_main():
    tasks = [
        asyncio.ensure_future(async_url(url))
        for url in urls
    ]
    for future in asyncio.as_completed(tasks):
        url = await future
        print(url)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(async_main())

