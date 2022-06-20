import urllib.request
import asyncio



urls = [
    'https://habr.com/ru',
    'https://rozetka.com.ua/ua/',
    'https://www.python.org/',
    'https://www.netflix.com/browse'
]


async def async_url(url):
    fille_name = 'fille1.txt'
    with open(fille_name, 'a') as f:
        f.writelines(f'start {url}\n')
        result = urllib.request.urlopen(url)
        f.writelines(str(result.getcode())+'\n')
    msg = f'Finished {url}'
    return msg

async def main(urls):
    coroutines = [async_url(url) for url in urls]
    completed, pending = await asyncio.wait(coroutines)
    for i in completed:
        print(i.result())


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(urls))
    event_loop.close()
