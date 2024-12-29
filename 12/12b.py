from collections import defaultdict, deque

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

    # 0: up, 1: right, 2: down, 3: left
    edges = defaultdict(list)
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
            edges[(x, y)].append(0)

        # down
        if isSameCrop(data, x, y + 1, target):
            queue.append((x, y + 1))
        else:
            edges[(x, y)].append(2)

        # left
        if isSameCrop(data, x - 1, y, target):
            queue.append((x - 1, y))
        else:
            edges[(x, y)].append(3)

        # right
        if isSameCrop(data, x + 1, y, target):
            queue.append((x + 1, y))
        else:
            edges[(x, y)].append(1)

    # Calculate the number of straight lines
    lines = 0
    visited = set()

    def calcLine(x, y, dir, visisted):
        if (x, y, dir) in visited:
            return

        visited.add((x, y, dir))
        if dir % 2 == 0:
            # Check left and right since the line is horizontal
            if (x - 1, y) in edges and dir in edges[(x - 1, y)]:
                calcLine(x - 1, y, dir, visited)
            if (x + 1, y) in edges and dir in edges[(x + 1, y)]:
                calcLine(x + 1, y, dir, visited)
        else:
            # Check up and down since the line is vertical
            if (x, y - 1) in edges and dir in edges[(x, y - 1)]:
                calcLine(x, y - 1, dir, visited)
            if (x, y + 1) in edges and dir in edges[(x, y + 1)]:
                calcLine(x, y + 1, dir, visited)

    # convert to normal dict
    edges = dict(edges)
    for (x, y), dirs in edges.items():
        for dir in dirs:
            if (x, y, dir) in visited:
                continue

            calcLine(x, y, dir, visited)
            lines += 1

    return area * lines


visited = set()
total = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) in visited:
            continue

        total += calcRegion(data, x, y, visited)

print(total)
