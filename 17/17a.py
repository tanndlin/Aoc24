import heapq

data = open('sample.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [tuple(map(int, i.split(','))) for i in data]

WIDTH = 71

grid = {}
for x in range(WIDTH):
    for y in range(WIDTH):
        grid[x, y] = False

for x, y in data[:1024]:
    grid[x, y] = True


def printGrid(visited):
    for y in range(WIDTH):
        for x in range(WIDTH):
            if (x, y) in visited:
                print('+', end='')
            else:
                print('#' if grid[x, y] else '.', end='')

        print()


def bfs():
    q = [(0, (0, 0))]
    visited = set()
    while q:
        cost, pos = heapq.heappop(q)
        if pos == (WIDTH - 1, WIDTH - 1):
            return cost

        x, y = pos
        if x < 0 or x >= WIDTH or y < 0 or y >= WIDTH:
            continue

        if grid[pos]:
            continue

        if pos in visited:
            continue

        visited.add(pos)
        # printGrid(visited)
        # print()

        heapq.heappush(q, (cost + 1, (pos[0], pos[1] - 1)))
        heapq.heappush(q, (cost + 1, (pos[0], pos[1] + 1)))
        heapq.heappush(q, (cost + 1, (pos[0] - 1, pos[1])))
        heapq.heappush(q, (cost + 1, (pos[0] + 1, pos[1])))

    return -1


printGrid([])
print(bfs())
