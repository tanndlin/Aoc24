data = open('input.txt', 'r').read().splitlines()

equations = []
for line in data:
    key, values = line.split(': ')
    if int(key) in equations:
        raise Exception('Duplicate key')
    equations.append((int(key), list(map(int, values.split(' ')))))


def canBeSolved(target, curValue, values, depth):
    if curValue > target:
        return False

    if depth == len(values):
        return curValue == target

    # Try adding
    if canBeSolved(target, curValue + values[depth], values, depth + 1):
        return True

    # Try multiplying
    if canBeSolved(target, curValue * values[depth], values, depth + 1):
        return True

    # Try concat
    if canBeSolved(target, int(str(curValue) + str(values[depth])), values, depth + 1):
        return True

    return False


total = 0
for eq in equations:
    key, values = eq
    if canBeSolved(key, values[0], values[1:], 0):
        total += key

print(total)
