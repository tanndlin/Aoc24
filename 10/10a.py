data = open('sample.txt', 'r').read().splitlines()
data = open('input.txt', 'r').read().splitlines()
data = [list(map(int, (n for n in line))) for line in data]


def calcScore(x, y, currentHeight, ends):
    if currentHeight == 9:
        ends.add((x, y))
        return

    # try up
    if y > 0 and data[y - 1][x] == currentHeight + 1:
        calcScore(x, y - 1, currentHeight + 1, ends)
    # try down
    if y < len(data) - 1 and data[y + 1][x] == currentHeight + 1:
        calcScore(x, y + 1, currentHeight + 1, ends)
    # try left
    if x > 0 and data[y][x - 1] == currentHeight + 1:
        calcScore(x - 1, y, currentHeight + 1, ends)
    # try right
    if x < len(data[y]) - 1 and data[y][x + 1] == currentHeight + 1:
        calcScore(x + 1, y, currentHeight + 1, ends)

    return len(ends)


total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            total += calcScore(x, y, 0, set())

print(total)
