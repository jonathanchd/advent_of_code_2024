import sys
import re
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')
p2 = 0
substr = r"(mul\(\d+,\d+\))|do\(\)|don't\(\)"
do = True
for line in lines:
    matches = [match.group() for match in re.finditer(substr, line)]
    for match in matches:
        print(match)
        if match == 'do()':
            do = True
        elif match == "don't()":
            do = False
        elif do:
            match = match[4:-1].split(',')
            p2 += int(match[0]) * int(match[1])
        
print(p2)