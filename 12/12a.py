from collections import deque

data = open('sample.txt', 'r').read().splitlines()
data = open('input.txt', 'r').read().splitlines()
data = [[j for j in i] for i in data]


def isSameCrop(data, x, y, target):
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return False

    return data[y][x] == target


def calcRegion(data, x, y, visited):
    if (x, y) in visited:
        return 0, 0

    queue = deque([(x, y)])
    target = data[y][x]
    area = 0
    perimeter = 0
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue

        area += 1
        visited.add((x, y))

        # up
        if isSameCrop(data, x, y - 1, target):
            queue.append((x, y - 1))
        else:
            perimeter += 1

        # down
        if isSameCrop(data, x, y + 1, target):
            queue.append((x, y + 1))
        else:
            perimeter += 1

        # left
        if isSameCrop(data, x - 1, y, target):
            queue.append((x - 1, y))
        else:
            perimeter += 1

        # right
        if isSameCrop(data, x + 1, y, target):
            queue.append((x + 1, y))
        else:
            perimeter += 1

    return area * perimeter


visited = set()
total = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) in visited:
            continue

        total += calcRegion(data, x, y, visited)

print(total)
