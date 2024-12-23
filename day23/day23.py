import sys
from collections import defaultdict
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

edges = [tuple(line.split('-')) for line in lines]

adj = defaultdict(set)

for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)

ans = 0

for i, ik in enumerate(adj.keys()):
    for j, jk in enumerate(adj.keys()):
        for k, kk in enumerate(adj.keys()):
            if i == j or j == k or i == k:
                continue
            if ik[0] != 't' and jk[0] != 't' and kk[0] != 't':
                continue
            if jk in adj[ik] and kk in adj[ik] and jk in adj[kk]:
                ans += 1

print(ans // 6)