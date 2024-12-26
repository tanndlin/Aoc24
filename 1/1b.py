from collections import defaultdict

data = open('input.txt', 'r').read()

a = []
b = defaultdict(int)

for i in data.split('\n'):
    if i == '':
        continue

    split = i.split('   ')
    a.append(int(split[0]))
    b[int(split[1])] += 1

s = 0
for aN in a:
    s += aN * b[aN]

print(s)
