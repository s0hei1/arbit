from asyncio import Queue, sleep, run

q = Queue()


async def init_data():
    for i in range(1, 7):
        await q.put(i)
        print(f"add {i}")
    await sleep(1)


async def receive_data():
    while not q.empty():
        data = await q.get()
        yield data


async def main():
    await init_data()

    async for i in receive_data():
        print(i)
        await sleep(2)


run(main())