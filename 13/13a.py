import re

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

    games.append((a, b, prize))


def play(a, b, prize):
    aX, aY = a
    bX, bY = b
    prizeX, prizeY = prize

    n = 0
    naX = 0
    naY = 0
    remainingX = prizeX
    remainingY = prizeY
    # k = n*a + m*b
    while naX < prizeX and naY < prizeY:
        # Solve for m
        if remainingX % bX == 0 and remainingY % bY == 0:
            mx = remainingX // bX
            my = remainingY // bY
            if mx == my:
                return (n, mx)

        n += 1
        naX += aX
        naY += aY
        remainingX -= aX
        remainingY -= aY

    # print('no solution')
    return (0, 0)


total = 0
for game in games:
    a, b = play(*game)
    print(a, b)
    total += 3 * a + b

print(total)
