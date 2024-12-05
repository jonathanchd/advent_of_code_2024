import sys
from collections import defaultdict, deque
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
        continue

    n = len(line)
    reordered = []
    inc = [0] * n
    mp = dict()
    for i in range(n):
        mp[line[i]] = i

    for val in line:
        if val not in reqs:
            continue
        for adj in reqs[val]:
            if adj in line:
                inc[mp[adj]] += 1
    queue = deque()
    for i in range(n):
        if inc[i] == 0:
            queue.append(i)
    while len(queue) != 0:
        for i in range(len(queue)):
            top = queue.popleft()
            reordered.append(line[top])
            if line[top] not in reqs:
                continue
            for adj in reqs[line[top]]:
                if adj in line:
                    inc[mp[adj]] -= 1
                    if inc[mp[adj]] == 0:
                        queue.append(mp[adj])
                        
    ans += reordered[len(reordered) // 2]
    print(reordered)

print(ans)
