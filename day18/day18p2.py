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

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def reachable():
    global grid
    dq = deque()
    visited = set()
    dq.append((0, 0))
    while len(dq) != 0:
        r, c = dq.popleft()
        if r == n - 1 and c == m - 1:
            return True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if good(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                dq.append((nr, nc))
                visited.add((nr, nc))
    return False

for r, c in lines:
    grid[r][c] = 1
    if not reachable():
        print(r, c)
        break
