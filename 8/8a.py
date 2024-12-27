from collections import defaultdict

data = open('test.txt', 'r').read().splitlines()
data = open('input.txt', 'r').read().splitlines()
data = [[j for j in i] for i in data]

radios = defaultdict(list)

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell != '.':
            radios[cell].append((x, y))


def calcAntinodes(r1, r2):
    r1x, r1y = r1
    r2x, r2y = r2

    dx = r1x - r2x
    dy = r1y - r2y

    # There are 2 possible antinodes
    a1 = (r1x + dx, r1y + dy)
    a2 = (r2x - dx, r2y - dy)

    return a1, a2


def isInBounds(pos):
    x, y = pos
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


antinodes = set()

for freq in radios:
    for i in range(len(radios[freq])):
        for j in range(i + 1, len(radios[freq])):
            anti = calcAntinodes(radios[freq][i], radios[freq][j])
            for a in anti:
                if isInBounds(a):
                    antinodes.add(a)

print(len(antinodes))

# def printResult():
#     for y, row in enumerate(data):
#         for x, cell in enumerate(row):
#             if (x, y) in antinodes:
#                 print('#', end='')
#             else:
#                 print(cell, end='')
#         print()


# printResult()
