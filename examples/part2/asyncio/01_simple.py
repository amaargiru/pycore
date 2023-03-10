import asyncio
from datetime import datetime


async def fun1(a, b):
    print(f"fun1 result: {a + b}")
    await asyncio.sleep(1)
    print("fun1 complete")


async def fun2(a, b):
    print(f"fun2 result: {a - b}")
    await asyncio.sleep(1)
    print("fun2 complete")


async def main():
    start_time = datetime.now()

    task1 = asyncio.create_task(fun1(3, 2))
    task2 = asyncio.create_task(fun2(3, 2))

    await asyncio.wait([task1, task2], return_when=asyncio.ALL_COMPLETED)

    duration_time = datetime.now() - start_time
    print(f"Total duration time: {duration_time}")


if __name__ == '__main__':
    asyncio.run(main())
