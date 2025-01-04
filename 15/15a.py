data = open('sample.txt').read().strip().split('\n\n')
data = open('input.txt').read().strip().split('\n\n')


# parse map
pos = None
grid = {}
for y, line in enumerate(data[0].splitlines()):
    for x, c in enumerate(line):
        grid[(x, y)] = c
        if c == '@':
            pos = (x, y)

# parse moves
# moves = []
# for line in data[1].splitlines():
#     moves.extend(i for i in line)

moves = [i for i in ''.join(data[1].splitlines())]


def moveDir(dir):
    global pos

    newX, newY = pos
    dx, dy = dir

    newX += dx
    newY += dy

    cell = grid.get((newX, newY))
    if cell == '.':
        grid[pos] = '.'
        pos = (newX, newY)
        grid[pos] = '@'
        return

    while cell == 'O':
        newX += dx
        newY += dy
        cell = grid.get((newX, newY))

    if cell == '.':
        # move all walls up
        # remove first one above
        grid[(newX, newY)] = 'O'
        grid[pos] = '.'
        pos = (pos[0] + dx, pos[1] + dy)
        grid[pos] = '@'
        return

    # wall
    return


def printGrid():
    width = max(x for x, y in grid) + 1
    height = max(y for x, y in grid) + 1
    for y in range(height):
        for x in range(width):
            print(grid[(x, y)], end='')
        print()


def doMove(move):
    global pos
    if move == '^':
        moveDir((0, -1))
    elif move == 'v':
        moveDir((0, 1))
    elif move == '<':
        moveDir((-1, 0))
    elif move == '>':
        moveDir((1, 0))


def calcScore():
    score = 0
    for pos, cell in grid.items():
        if cell == 'O':
            score += 100 * pos[1] + pos[0]
    return score


for move in moves:
    doMove(move)

print(calcScore())
