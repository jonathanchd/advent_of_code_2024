import sys
from collections import deque
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

lines = [tuple(map(int, line.split(','))) for line in lines]

def good(r, c):
    return 0 <= r < n and 0 <= c < m

n, m = 71, 71

grid = [[0] * m for i in range(n)]
for i in range(1024):
    grid[lines[i][0]][lines[i][1]] = 1

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

dq = deque()
visited = set()
dq.append((0, 0, 0))
while len(dq) != 0:
    dist, r, c = dq.popleft()
    if r == n - 1 and c == m - 1:
        ans = dist
        break
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if good(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
            dq.append((dist + 1, nr, nc))
            visited.add((nr, nc))

print(ans)
