import time
from collections import defaultdict
from functools import lru_cache

import numpy
import numpy as np

orders, updates = open('input.txt', 'r').read().split('\n\n')
orders = [list(map(int, x.split('|'))) for x in orders.splitlines()]
updates = [list(map(int, x.split(','))) for x in updates.splitlines()]

precedence = defaultdict(set)

for order in orders:
    a, b = order
    precedence[b].add(a)


# a must come before b... ie: b is a parent of a
@lru_cache(None)
def isParent(a, b):
    if a in precedence[b]:
        return True

    return False


def isInOrder(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            a = update[i]
            b = update[j]
            # If b must come before a, then it is not in order
            if isParent(b, a):
                print(a, b)
                return False
    return True


s = 0
for update in updates:
    if isInOrder(update):
        # add s + the middle number of the update
        midIndex = len(update) // 2
        s += update[midIndex]

print(s)
