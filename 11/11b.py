import time
from collections import defaultdict
from functools import lru_cache
from math import floor, log10

data = list(map(int, open('input.txt', 'r').read().split()))


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = floor((time.time() - start) * 1000)
        print(f'{func.__name__} executed in {end}ms')
        return result

    return wrapper


@lru_cache
def doStone(n):
    if n == 0:
        return (1,)

    log = log10(n)
    hasEvenNumberOfDigits = floor(log) % 2 == 1
    if hasEvenNumberOfDigits:
        leftHalf = n // 10 ** (floor(log / 2) + 1)
        rightHalf = n % 10 ** (floor(log / 2) + 1)
        return (leftHalf, rightHalf)

    return (n * 2024,)


def exhaustStone(stone, stones):
    newStones = defaultdict(int)
    result = doStone(stone)
    numTimes = stones[stone]

    for newStone in result:
        newStones[newStone] += numTimes

    return newStones


@timeit
def main(data, GENERATIONS=75):
    stones = defaultdict(int)
    for stone in data:
        stones[stone] += 1

    for _ in range(GENERATIONS):
        newStones = defaultdict(int)
        for stone in stones:
            result = exhaustStone(stone, stones)
            for newStone, amount in result.items():
                newStones[newStone] += amount

        stones = newStones

    return stones


if __name__ == '__main__':
    result = main(data, 75)
    total = sum(result.values())
    # print(result)
    print(total)
