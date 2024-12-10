import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')
lines = [[int(x) for x in line] for line in lines]

n, m = len(lines), len(lines[0])

def good(r, c):
    global n, m
    return r >= 0 and r < n and c >= 0 and c < m

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

ans = 0

def search(r, c, visited):
    global lines, ans, dr, dc
    if visited[r][c]:
        return
    visited[r][c] = True
    if lines[r][c] == 9:
        ans += 1
        visited[r][c] = False
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if good(nr, nc) and lines[r][c] + 1 == lines[nr][nc]:
            search(nr, nc, visited)
    visited[r][c] = False

for i in range(n):
    for j in range(m):
        if lines[i][j] != 0:
            continue
        visited = [[False] * n for i in range(m)]
        search(i, j, visited)

print(ans)