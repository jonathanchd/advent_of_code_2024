import sys
import re
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')
p1 = 0
substr = r"mul\(\d+,\d+\)"
for line in lines:
    matches = [match.group() for match in re.finditer(substr, line)]
    for match in matches:
        match = match[4:-1].split(',')
        p1 += int(match[0]) * int(match[1])

print(p1)