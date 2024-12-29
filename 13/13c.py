import re
from math import floor, gcd
from time import time

data = open('sample.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')
games = []

aRegex = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
bRegex = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
prizeRegex = re.compile(r'Prize: X=(\d+), Y=(\d+)')
for game in data:
    a, b, prize = game.split('\n')
    a = tuple(map(int, aRegex.search(a).groups()))
    b = tuple(map(int, bRegex.search(b).groups()))
    prize = tuple(map(int, prizeRegex.search(prize).groups()))
    N = 10000000000000
    prize = (prize[0] + N, prize[1] + N)

    games.append((a, b, prize))


def play(a, b, prize):
    aX, aY = a
    bX, bY = b
    prizeX, prizeY = prize

    n = (bX * prizeY - bY * prizeX) / (aY * bX - bY * aX)
    if int(n) != n:
        return (0, 0)

    m = (prizeX - n * aX) / bX
    if int(m) != m:
        return (0, 0)

    return (int(n), int(m))


total = 0
for game in games:
    a, b = play(*game)
    total += 3 * a + b

print(total)
