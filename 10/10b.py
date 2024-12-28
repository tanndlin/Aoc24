data = open('sample.txt', 'r').read().splitlines()
data = open('input.txt', 'r').read().splitlines()
data = [list(map(int, (n for n in line))) for line in data]


def calcScore(x, y, currentHeight):
    if currentHeight == 9:
        return 1

    score = 0
    # try up
    if y > 0 and data[y - 1][x] == currentHeight + 1:
        score += calcScore(x, y - 1, currentHeight + 1)
    # try down
    if y < len(data) - 1 and data[y + 1][x] == currentHeight + 1:
        score += calcScore(x, y + 1, currentHeight + 1)
    # try left
    if x > 0 and data[y][x - 1] == currentHeight + 1:
        score += calcScore(x - 1, y, currentHeight + 1)
    # try right
    if x < len(data[y]) - 1 and data[y][x + 1] == currentHeight + 1:
        score += calcScore(x + 1, y, currentHeight + 1)

    return score


total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            total += calcScore(x, y, 0)

print(total)
