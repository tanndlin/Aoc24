data = open('input.txt', 'r').read().splitlines()
data = [[j for j in i] for i in data]

obstacles = set()
visited = set()
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0


def turnRight():
    global direction
    direction = (direction + 1) % 4


def isInBounds(x, y):
    return x >= 0 and y >= 0 and x < len(data[0]) and y < len(data)


def calcVisited(x, y):
    while isInBounds(x, y):
        visited.add((x, y))

        nextPos = (x + directions[direction][0], y + directions[direction][1])
        if nextPos in obstacles:
            turnRight()
            continue

        x, y = nextPos


# Parse map
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '#':
            obstacles.add((x, y))
        if data[y][x] == '^':
            start = (x, y)

calcVisited(start[0], start[1])
print(len(visited))
