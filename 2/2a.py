data = open('input.txt', 'r').read().splitlines()


def isSafe(nums):
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

    allIncreasingOrDecreasing = all((i > 0 for i in diffs)) or all((i < 0 for i in diffs))
    if not allIncreasingOrDecreasing:
        return False

    absDiffs = map(abs, diffs)
    for diff in absDiffs:
        if diff > 3:
            return False
        if diff < 1:
            return False

    return True


safe = 0

for line in data:
    nums = list(map(int, line.split()))
    if isSafe(nums):
        safe += 1
    else:
        # Try removing one number and checking if it's safe
        for i in range(len(nums)):
            if isSafe(nums[:i] + nums[i + 1 :]):
                safe += 1
                break

print(safe)
