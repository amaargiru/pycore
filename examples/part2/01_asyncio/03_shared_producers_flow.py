import asyncio
import random
from datetime import datetime

# Пример накопления данных от двух асинхронных периодических задач в одной разделяемой структуре данных asyncio.Queue().

async def produce_small_random(queue):
    while True:
        await asyncio.sleep(0.5)
        r: int = random.randint(1, 9)
        print(f'Small random produced {r}')
        await queue.put(r)


async def produce_big_random(queue):
    while True:
        await asyncio.sleep(1)
        r: int = random.randint(100, 999)
        print(f'Big random produced {r}')
        await queue.put(r)


async def main():
    q = asyncio.Queue()
    start_time = datetime.now()

    small_random_task = asyncio.create_task(produce_small_random(q))
    big_random_task = asyncio.create_task(produce_big_random(q))

    await asyncio.sleep(10)

    small_random_task.cancel()
    big_random_task.cancel()

    # Dumping asyncio.queue into list
    randl: list[int] = []
    while q.qsize() > 0:
        randl.append(await q.get())
        q.task_done()

    duration_time = datetime.now() - start_time

    print(f'Total queue = {randl}')
    print(f'Total duration time: {duration_time}')


if __name__ == '__main__':
    asyncio.run(main())
