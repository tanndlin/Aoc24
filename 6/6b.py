data = open('input.txt', 'r').read().splitlines()
data = [[j for j in i] for i in data]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def isInBounds(x, y):
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


def causesLoop():
    visited = set()
    direction = 0
    x, y = start

    while isInBounds(x, y):
        if (x, y, direction) in visited:
            return True

        visited.add((x, y, direction))
        nextPos = (x + directions[direction][0], y + directions[direction][1])
        if not isInBounds(*nextPos):
            return False

        if data[nextPos[1]][nextPos[0]] == '#':
            direction = (direction + 1) % 4
        else:
            x, y = nextPos

    return False


# Parse map
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '^':
            start = (x, y)

total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '.':
            data[y][x] = '#'
            if causesLoop():
                total += 1
            data[y][x] = '.'

print(total)
