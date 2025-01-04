import re

data = open('sample.txt', 'r').read().splitlines()
data = open('input.txt', 'r').read().splitlines()
regex = re.compile(r'p=(-?\d+,-?\d+) v=(-?\d+,-?\d+)')

WIDTH = 101
HEIGHT = 103

robots = []
for robot in data:
    postion, velocity = regex.search(robot).groups()
    postion = tuple(map(int, postion.split(',')))
    velocity = tuple(map(int, velocity.split(',')))

    robots.append((postion, velocity))


def iteration():
    for robot in robots:
        postion, velocity = robot
        x, y = postion
        dx, dy = velocity
        x += dx
        y += dy
        postion = (x % WIDTH, y % HEIGHT)
        robot = (postion, velocity)


def createGrid():
    grid = {}
    for y in range(HEIGHT):
        for x in range(WIDTH):
            grid[(x, y)] = []

    for robot in robots:
        postion, _ = robot
        grid[postion].append(robot)

    return grid


def calcSafetyFactor():
    topLeft = 0
    topRight = 0
    bottomLeft = 0
    bottomRight = 0

    for robot in robots:
        postion, _ = robot
        x, y = postion
        isTopHalf = y < HEIGHT // 2
        isBottomHalf = y > HEIGHT // 2
        isLeft = x < WIDTH // 2
        isRight = x > WIDTH // 2

        # Top left
        if isTopHalf and isLeft:
            topLeft += 1
        # Top right
        if isTopHalf and isRight:
            topRight += 1
        # Bottom left
        if isBottomHalf and isLeft:
            bottomLeft += 1
        # Bottom right
        if isBottomHalf and isRight:
            bottomRight += 1

    return (topLeft or 1) * (topRight or 1) * (bottomLeft or 1) * (bottomRight or 1)


for i in range(100):
    iteration()

print(calcSafetyFactor())
