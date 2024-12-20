import sys
from collections import deque
infile = sys.argv[1]
D = open(infile).read().strip()

grid = [[x for x in line] for line in D.split('\n')]
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E':
            er, ec = i, j

def good(r, c):
    return 0 <= r < n and 0 <= c < m

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dists = dict()
dists[(er, ec)] = 0
def findDists():
    dq = deque()
    dq.append((0, er, ec))
    while len(dq) != 0:
        dist, r, c = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not good(nr, nc) or grid[nr][nc] == '#' or (nr, nc) in dists:
                continue
            if grid[nr][nc] == 'S':
                dists[(nr, nc)] = dist + 1
                return dist + 1
            dists[(nr, nc)] = dist + 1
            dq.append((dist + 1, nr, nc))
    return -1

d = findDists()
ans = 0
dists = list(dists.items())

for i in range(len(dists)):
    for j in range(i + 1, len(dists)):
        (ar, ac), ad = dists[i]
        (br, bc), bd = dists[j]
        manhatDist = abs(ar - br) + abs(ac - bc)
        if manhatDist > 20:
            continue
        save = abs(ad - bd) - manhatDist
        if save >= 100:
            ans += 1

print(ans)