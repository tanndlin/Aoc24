from collections import defaultdict

data = open('sample.txt').read().strip().split('\n\n')
data = open('sample2.txt').read().strip().split('\n\n')
data = open('input.txt').read().strip().split('\n\n')


# parse map
pos = None
grid = {}
for y, line in enumerate(data[0].splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            grid[(2 * x, y)] = '#'
            grid[(2 * x + 1, y)] = '#'
        if c == '.':
            grid[(2 * x, y)] = '.'
            grid[(2 * x + 1, y)] = '.'
        if c == 'O':
            grid[(2 * x, y)] = '['
            grid[(2 * x + 1, y)] = ']'
        if c == '@':
            pos = (2 * x, y)
            grid[(2 * x, y)] = '@'
            grid[(2 * x + 1, y)] = '.'

# parse moves
# moves = []
# for line in data[1].splitlines():
#     moves.extend(i for i in line)

moves = [i for i in ''.join(data[1].splitlines())]


def moveVeritcal(dy):
    global pos
    newX, newY = pos
    newY += dy

    # Open space
    if grid[(newX, newY)] == '.':
        grid[pos] = '.'
        pos = (newX, newY)
        grid[pos] = '@'
        return

    # Wall
    if grid[(newX, newY)] == '#':
        return

    #  Must be a box
    boxType = grid[newX, newY]
    needToBeClear = defaultdict(set)
    needToBeClear[newY].add(newX)
    if boxType == '[':
        needToBeClear[newY].add(newX + 1)
    else:
        needToBeClear[newY].add(newX - 1)

    def getObjectsInRow(xs, y):
        objects = set()
        for x in xs:
            objects.add(grid[x, y])

        return objects

    objects = getObjectsInRow(needToBeClear[newY], newY)
    while '#' not in objects and objects != {'.'}:
        newY += dy
        objects = getObjectsInRow(needToBeClear[newY - dy], newY)
        for x in needToBeClear[newY - dy]:
            # If the space above is a box, need to append these xs to the list
            if grid[x, newY] == '[':
                needToBeClear[newY].add(x)
                needToBeClear[newY].add(x + 1)
            if grid[x, newY] == ']':
                needToBeClear[newY].add(x)
                needToBeClear[newY].add(x - 1)

    # We have reach either an entirely clear row, or there is a wall in the way
    if '#' in objects:
        return  # cant move

    # Can move
    oldGrid = grid.copy()
    needToBeClear = dict(needToBeClear)
    for y in needToBeClear:
        for x in needToBeClear[y]:
            was = oldGrid[(x, y)]

            # There was a not a wall beneath and needs to be removed
            if y - dy not in needToBeClear or x not in needToBeClear[y - dy]:
                grid[(x, y)] = '.'
            grid[(x, y + dy)] = was

    grid[pos] = '.'
    pos = (newX, pos[1] + dy)
    grid[pos] = '@'


def moveHorizontal(dx):
    global pos
    newX, newY = pos
    newX += dx

    # Open space
    if grid[(newX, newY)] == '.':
        grid[pos] = '.'
        pos = (newX, newY)
        grid[pos] = '@'
        return

    # Wall
    if grid[(newX, newY)] == '#':
        return

    # Must be a box
    cell = grid[(newX, newY)]
    while cell == '[' or cell == ']':
        newX += dx
        cell = grid[(newX, newY)]

    # Wall
    if cell == '#':
        return

    # Move all boxes

    if dx == 1:
        for x in range(newX, pos[0] + 1, -1):
            grid[x, newY] = grid[x - dx, newY]

        grid[pos] = '.'
        pos = (pos[0] + dx, newY)
        grid[pos] = '@'

    if dx == -1:
        for x in range(newX, pos[0] - 1):
            grid[x, newY] = grid[x - dx, newY]

        grid[pos] = '.'
        pos = (pos[0] + dx, newY)
        grid[pos] = '@'


def printGrid():
    width = max(x for x, y in grid) + 1
    height = max(y for x, y in grid) + 1

    print(width, height)
    for y in range(height):
        for x in range(width):
            print(grid[(x, y)], end='')
        print()


def doMove(move):
    if move == '^':
        moveVeritcal(-1)
    elif move == 'v':
        moveVeritcal(1)
    elif move == '>':
        moveHorizontal(1)
    elif move == '<':
        moveHorizontal(-1)


def calcScore():
    score = 0
    for pos, cell in grid.items():
        if cell == '[':
            score += 100 * pos[1] + pos[0]
    return score


for move in moves:
    doMove(move)
    # printGrid()

print(calcScore())
