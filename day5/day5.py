import sys
from collections import defaultdict
infile = sys.argv[1]
D = open(infile).read().strip()

thing = 1176
# thing = 21

lines = D.split('\n')
req = lines[:thing]
inp = lines[thing + 1:]

reqs = defaultdict(set)

for r in req:
    r = r.split('|')
    a = int(r[0])
    b = int(r[1])
    reqs[a].add(b)

ans = 0

for line in inp:
    good = True
    line = list(map(int, line.split(',')))
    for i in range(len(line)):
        for j in range(i):
            if line[j] in reqs[line[i]]:
                good = False
                break
        if not good:
            break

    if good:
        ans += int(line[len(line) // 2])

print(ans)
