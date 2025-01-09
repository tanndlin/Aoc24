import heapq
import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

data = open('sample2.txt').read().splitlines()
data = open('sample.txt').read().splitlines()
data = open('input.txt').read().splitlines()

start = None
end = None
grid = {}
scores = {}

for y, line in enumerate(data):
    for x, cell in enumerate(line):
        grid[x, y] = cell
        if cell == 'S':
            start = (x, y)
        if cell == 'E':
            end = (x, y)

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    q = [(0, (start, 2, [start]))]
    visited = set()
    while q:
        cost, (pos, dir, path) = heapq.heappop(q)
        if pos == end:
            return cost, path
        if (pos, dir) in visited:
            continue
        if grid[pos] == '#':
            continue

        visited.add((pos, dir))

        # Try rotating
        for new_dir, (dx, dy) in enumerate(dirs):
            if new_dir != dir:
                heapq.heappush(q, (cost + 1000, (pos, new_dir, path)))

        # Try moving forward
        dx, dy = dirs[dir]
        new_pos = (pos[0] + dx, pos[1] + dy)
        heapq.heappush(q, (cost + 1, (new_pos, dir, path + [new_pos])))

    return None, None


cost, places = bfs()
print(cost)
print(len(places))
assert cost == 88416, f'Cost was {cost}, should be 88416'
