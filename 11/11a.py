data = list(map(int, open('input.txt', 'r').read().split()))


def doStone(n):
    if n == 0:
        return [1]

    nAsStr = str(n)
    if len(nAsStr) % 2 == 0:
        leftHalf = nAsStr[: len(nAsStr) // 2]
        rightHalf = nAsStr[len(nAsStr) // 2 :]
        return [int(leftHalf), int(rightHalf)]

    return [n * 2024]


for i in range(25):
    oldData = data.copy()
    data = []
    for n in oldData:
        data += doStone(n)

print(len(data))
