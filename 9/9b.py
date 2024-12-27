data = [int(n) for n in open('sample.txt', 'r').read().strip()]
data = [int(n) for n in open('input.txt', 'r').read().strip()]


def createDisk():
    flag = True
    id = 0
    disk = {}
    curIndex = 0
    for size in data:
        if flag:
            disk[curIndex] = (id, size)
            id += 1
        else:
            disk[curIndex] = (None, size)
        flag = not flag
        curIndex += size

    return disk, id - 1


def getFile(disk, id):
    for key in disk:
        if disk[key][0] == id:
            return key
    return None


def getFreeSpace(disk, minSize):
    for key in sorted(disk.keys()):
        if disk[key][0] is None and disk[key][1] >= minSize:
            return key
    return None


def removeFile(disk, key):
    # If the entry before was free, combine them
    curSize = disk[key][1]
    keyBefore = max((k for k in disk if k < key), default=None)
    nextKey = key + curSize
    changed = False
    if keyBefore is not None and disk[keyBefore][0] is None:
        disk[keyBefore] = (None, disk[keyBefore][1] + curSize)
        del disk[key]
        key = keyBefore
        changed = True

    # If the entry after was free, combine them
    if nextKey in disk and disk[nextKey][0] is None:
        disk[key] = (None, disk[nextKey][1] + disk[key][1])
        del disk[nextKey]
        changed = True

    if not changed:
        disk[key] = (None, curSize)

    return disk


def moveFile(disk, id):
    key = getFile(disk, id)
    if key is None:
        return disk

    size = disk[key][1]
    freeSpace = getFreeSpace(disk, size)
    if freeSpace is None or freeSpace >= key:
        return disk

    oldFreeSpaceSize = disk[freeSpace][1]
    disk[freeSpace] = (id, size)
    if oldFreeSpaceSize > size:
        disk[freeSpace + size] = (None, oldFreeSpaceSize - size)

    return removeFile(disk, key)


def checkSum(disk):
    total = 0
    for key in disk:
        if disk[key][0] is None:
            continue

        id, size = disk[key]
        for i in range(size):
            total += (key + i) * id

    return total


def printDisk(disk):
    for key in sorted(disk.keys()):
        id, size = disk[key]
        for i in range(size):
            if id is None:
                print('.', end='')
            else:
                print(id, end='')
    print()


disk, maxID = createDisk()
for i in range(maxID, -1, -1):
    disk = moveFile(disk, i)


print(checkSum(disk))
