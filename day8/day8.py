import sys
from collections import defaultdict
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

#thing closer to b than a
def getNode(a, b):
    difR, difC = b[0] - a[0], b[1] - a[1]
    return b[0] + difR, b[1] + difC

def good(r, c):
    global n
    global m
    return r >= 0 and r < n and c >= 0 and c < m

n = len(lines)
m = len(lines[0])
locs = defaultdict(list)
for i in range(n):
    for j in range(m):
        if lines[i][j] == '.':
            continue
        locs[lines[i][j]].append((i, j))

ans = set()

for lis in locs.values():
    k = len(lis)
    for i in range(k):
        for j in range(i + 1, k):
            a = getNode(lis[i], lis[j])
            b = getNode(lis[j], lis[i])
            if good(a[0], a[1]):
                ans.add(a)
            if good(b[0], b[1]):
                ans.add(b)
                
print(len(ans))