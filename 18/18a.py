data = open('sample.txt').read().split('\n\n')
data = open('input.txt').read().split('\n\n')

patterns = data[0].split(', ')
goals = data[1].splitlines()


def isPossible(towel: str):
    if towel == '':
        return True

    for pattern in patterns:
        if towel.startswith(pattern):
            if isPossible(towel[len(pattern) :]):
                return True

    return False


def solve():
    total = 0
    for towel in goals:
        total += isPossible(towel)

    return total


print(solve())
