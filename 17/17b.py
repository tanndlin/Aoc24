import heapq

data = open('sample.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [tuple(map(int, i.split(','))) for i in data]

WIDTH = 71

grid = {}
for x in range(WIDTH):
    for y in range(WIDTH):
        grid[x, y] = False


def bfs(grid):
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


i = 0
while True:
    x, y = data[i]
    grid[x, y] = True

    if bfs(grid) == -1:
        print(f'{x},{y}')
        break

    i += 1
