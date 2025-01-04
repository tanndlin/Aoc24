import os
import re

import cv2
import numpy as np

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
    for i, robot in enumerate(robots):
        postion, velocity = robot
        x, y = postion
        dx, dy = velocity
        x += dx
        y += dy
        postion = (x % WIDTH, y % HEIGHT)
        robots[i] = (postion, velocity)


def createGrid():
    grid = {}
    for y in range(HEIGHT):
        for x in range(WIDTH):
            grid[(x, y)] = []

    for robot in robots:
        postion, _ = robot
        grid[postion].append(robot)

    return grid


def gridToImage(grid):
    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[(x, y)]:
                img[y, x] = [255, 255, 255]
    return img


# remove all jpgs in images folder
for file in os.listdir('images'):
    if file.endswith('.jpg'):
        os.remove(f'images\\{file}')


i = 0
for j in range(5000):
    iteration()
    i += 1

for j in range(5000):
    iteration()
    i += 1
    print(f'Iteration: {i}')
    grid = createGrid()
    img = gridToImage(grid)

    # upscale image with nearest neighbor interpolation to double the size
    img = cv2.resize(img, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
    # Save image
    if not cv2.imwrite(f'images\\img{i}.jpg', img):
        raise Exception('Could not save image')
