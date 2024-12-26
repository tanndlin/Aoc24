import re

data = open('input.txt', 'r').read().splitlines()

regex = r'mul\(\d+,\d+\)'
s = 0
for line in data:
    # Find all occurrences of the regex
    matches = re.findall(regex, line)
    for match in matches:
        # Split the match by the comma
        a, b = map(int, match[4:-1].split(','))
        # Multiply the two numbers
        s += a * b

print(s)
