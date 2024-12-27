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
    return a in precedence[b]


def isInOrder(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            a = update[i]
            b = update[j]
            # If b must come before a, then it is not in order
            if b in precedence[a]:
                return False
    return True


def getTopMost(nums):
    possible = set(nums)

    # Find the number or numbers that must come before all else
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = nums[i]
            b = nums[j]
            if isParent(b, a):
                # Left cannot be the top most
                if a in possible:
                    possible.remove(a)
            if isParent(a, b):
                # Right cannot be the top most
                if b in possible:
                    possible.remove(b)

    return possible


def fix(update):
    fixed = [-1] * len(update)
    index = len(update) - 1
    left = set(update)

    # top most is the one that needs to come before all else
    while len(left) > 0:
        topMost = getTopMost(list(left))
        for n in topMost:
            fixed[index] = n
            index -= 1
            left.remove(n)

    if any(x == -1 for x in fixed):
        raise ValueError('Could not fix')
    return fixed


s = 0
for update in updates:
    if isInOrder(update):
        continue

    fixed = fix(update)
    midIndex = len(fixed) // 2
    s += fixed[midIndex]

print(s)
