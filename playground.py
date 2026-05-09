import asyncio

async def yield_a():
    for c in "abcdefghi":
        await asyncio.sleep(0)
        yield c

async def yield_b():
    for n in range(1, 10): 
        yield n

async def consume(gen):
    async for item in gen:
        print(item)

async def main():
    # create tasks that consume the generators
    task1 = asyncio.create_task(consume(yield_a()))
    task2 = asyncio.create_task(consume(yield_b()))
    await asyncio.gather(task1, task2)

asyncio.run(main())