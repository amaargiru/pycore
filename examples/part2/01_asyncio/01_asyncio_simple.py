import asyncio
import time
from time import perf_counter


# Простейший пример, одновременный запуск двух функций, последовательное выполнение которых в "синхронном" мире заняло бы 2 секунды,
# но в "асинхронном" мире они выполняются приблизительно за 1 секунду.

# Без asyncio, просто две функции с имитацией некоторого полезного вычисления и последующего ожидания
def fun1():
    sumi: int = 0

    for i in range(1000_000):
        sumi += i

    time.sleep(1)

    print(f'Sum: {sumi}')


def fun2():
    producti: int = 1

    for i in range(1, 25):
        producti = i * producti

    time.sleep(1)

    print(f'Product: {producti}')


start_time = perf_counter()

fun1()
fun2()

duration = perf_counter() - start_time
print(f'Total duration: {duration} seconds')


# С asyncio
async def afun1():
    sumi: int = 0

    for i in range(1000_000):
        sumi += i

    await asyncio.sleep(1)

    print(f'Sum: {sumi}')


async def afun2():
    producti: int = 1

    for i in range(1, 25):
        producti = i * producti

    await asyncio.sleep(1)

    print(f'Product: {producti}')


async def amain():
    task1 = asyncio.create_task(afun1())
    task2 = asyncio.create_task(afun2())

    await task1
    await task2


start_time = perf_counter()

asyncio.run(amain())

duration = perf_counter() - start_time
print(f'Total duration: {duration} seconds')
