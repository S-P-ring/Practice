import asyncio


async def handle_echo(reader, writter):
    data = await reader.read(20)
    n1, n2 = (data.decode()).split(' ')
    n1 = int(n1)
    n2 = int(n2)
    sum = n1 + n2
    writter.write(sum)
    await writter.drain()

    writter.close


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8000)

    async with server:
        await server.serve_forever()


asyncio.run(main())
