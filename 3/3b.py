import re

data = open('input.txt', 'r').read().splitlines()

regex = r'mul\(\d+,\d+\)'


def min2(a, b):
    if a == -1:
        return b
    if b == -1:
        return a

    return min(a, b)


def min3(a, b, c):
    return min2(a, min2(b, c))


def getNextOccurance(line):
    dont = 'don\'t()'
    do = 'do()'

    dontIndex = line.find(dont)
    doIndex = line.find(do)
    match = re.search(regex, line)
    mulIndex = -1 if match is None else match.start()

    # Check which of the 3 is first, but not -1
    return min3(dontIndex, doIndex, mulIndex)


def getState(line):
    global enabled
    if line.startswith('don\'t()'):
        enabled = False
    elif line.startswith('do()'):
        enabled = True


s = 0
enabled = True
for line in data:
    index = getNextOccurance(line)
    while index != -1:
        line = line[index:]
        getState(line)
        # print(isMul)
        # print(line)
        if enabled:
            # Find first occurrence of the regex
            match = re.search(regex, line)
            # Split the match by the comma
            a, b = map(int, match[0][4:-1].split(','))
            # Multiply the two numbers
            s += a * b
            line = line[match.end() :]
        else:
            line = line[1:]

        index = getNextOccurance(line)

print(s)
