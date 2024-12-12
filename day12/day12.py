import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

n, m = len(lines), len(lines[0])

visited = [[False] * m for _ in range(n)]

def good(r, c):
    return 0 <= r < n and 0 <= c < m

ans = 0
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        area, perim = 0, 0
        def search(r, c):
            global area, perim, lines, visited
            if visited[r][c]:
                return
            visited[r][c] = True
            area += 1
            p = 4
            for _ in range(4):
                nr = r + dr[_]
                nc = c + dc[_]
                if good(nr, nc) and lines[nr][nc] == lines[i][j]:
                    p -= 1
                    search(nr, nc)
            perim += p
        search(i, j)
        ans += area * perim

print(ans)