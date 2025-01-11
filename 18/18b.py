from functools import lru_cache

data = open('sample.txt').read().split('\n\n')
data = open('input.txt').read().split('\n\n')

patterns = data[0].split(', ')
goals = data[1].splitlines()


@lru_cache
def isPossible(towel: str):
    if towel == '':
        return 1

    ways = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            ways += isPossible(towel[len(pattern) :])

    return ways


def solve():
    total = 0
    for towel in goals:
        total += isPossible(towel)

    return total


print(solve())
