import re
from math import floor, gcd
from time import time

data = open('input.txt', 'r').read().split('\n\n')
data = open('sample.txt', 'r').read().split('\n\n')
games = []

aRegex = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
bRegex = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
prizeRegex = re.compile(r'Prize: X=(\d+), Y=(\d+)')
for game in data:
    a, b, prize = game.split('\n')
    a = tuple(map(int, aRegex.search(a).groups()))
    b = tuple(map(int, bRegex.search(b).groups()))
    prize = tuple(map(int, prizeRegex.search(prize).groups()))
    # N = 10000000000000
    N = 10000000000
    prize = (prize[0] + N, prize[1] + N)

    games.append((a, b, prize))


def play(a, b, prize):
    aX, aY = a
    bX, bY = b
    prizeX, prizeY = prize

    n = 0
    naX = 0
    naY = 0
    mbX = prizeX - naX
    mbY = prizeY - naY

    # prize = n*a + m*b
    # prizeX = n*aX + m*bX
    # prizeY = n*aY + m*bY
    # prizeX = naX + mbX
    # prizeY = naY + mbY

    while mbX % bX != 0:
        if mbX < 0:
            print('no solution')
            return (0, 0)

        n += 1
        naX += aX * 1
        naY += aY * 1
        mbX -= aX * 1
        mbY -= aY * 1

    iterations = bX // gcd(aX, bX)
    while naX < prizeX and naY < prizeY:
        # print(n)
        # Solve for m
        if mbX % bX == 0 and mbY % bY == 0:
            mx = mbX // bX
            if mx * bY == mbY:
                print(f'{n} {mx}')
                return (n, mx)

        n += iterations
        naX += aX * iterations
        naY += aY * iterations
        mbX -= aX * iterations
        mbY -= aY * iterations

    print('no solution')
    return (0, 0)


# total = 0
# for game in games:
#     print(game)
#     a, b = play(*game)
#     total += 3 * a + b

# print(total)


start = time()
print(play(*games[0]))
end = floor((time() - start) * 1000)
print(f'executed in {end}ms')
