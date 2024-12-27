data = [int(n) for n in open('sample.txt', 'r').read().strip()]
data = [int(n) for n in open('input.txt', 'r').read().strip()]
print(data)


def checksum(l):
    total = 0
    for pos, id in enumerate(l):
        if id is None:
            return total

        total += pos * id

    return total


l = []
# if true, indicates file size, if false indicates the size of free space
flag = True
id = 0

for size in data:
    if flag:
        for i in range(size):
            l.append(id)
        id += 1

    if not flag:
        for i in range(size):
            l.append(None)

    flag = not flag

print(l)
left = 0
right = len(l) - 1
while left < right:
    if l[left] is not None:
        left += 1
        continue

    if l[right] is None:
        right -= 1
        continue

    l[left], l[right] = l[right], l[left]

print(l)
print(checksum(l))
