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
    nodes = []
    r1x, r1y = r1
    r2x, r2y = r2

    dx = r1x - r2x
    dy = r1y - r2y

    # There are 2 possible antinodes
    a1 = r1
    while isInBounds(a1):
        nodes.append(a1)
        a1 = (a1[0] + dx, a1[1] + dy)
    a2 = r2
    while isInBounds(a2):
        nodes.append(a2)
        a2 = (a2[0] - dx, a2[1] - dy)

    return nodes


def isInBounds(pos):
    x, y = pos
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


antinodes = set()

for freq in radios:
    for i in range(len(radios[freq])):
        for j in range(i + 1, len(radios[freq])):
            anti = calcAntinodes(radios[freq][i], radios[freq][j])
            for a in anti:
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
