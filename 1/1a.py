data = open('input.txt', 'r').read()

a = []
b = []

for i in data.split('\n'):
    if i == '':
        continue

    split = i.split('   ')
    a.append(int(split[0]))
    b.append(int(split[1]))

a.sort()
b.sort()

s = 0
for aN, bN in zip(a, b):
    s += abs(aN - bN)

print(s)
