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
        area = 0
        #set to keep track of which sides are open for each cell
        #rip memory usage
        cnt = [[0] * m for i in range(n)]
        def search(r, c):
            global area, lines, visited, cnt
            if visited[r][c]:
                return
            visited[r][c] = True
            cnt[r][c] = set([0, 1, 2, 3])
            area += 1
            p = 4
            for _ in range(4):
                nr = r + dr[_]
                nc = c + dc[_]
                if good(nr, nc) and lines[nr][nc] == lines[i][j]:
                    p -= 1
                    search(nr, nc)
                    cnt[r][c].remove(_)

        search(i, j)
        sides = 0
        for r in range(n):
            for c in range(m):
                if type(cnt[r][c]) == int or len(cnt[r][c]) == 0:
                    continue
                sides += len(cnt[r][c])
                
                for side in cnt[r][c]:
                    def traverseEdge(cR, cC, tr, tc):
                        global side, lines, r, c
                        while True:
                            if not good(cR, cC) or lines[cR][cC] != lines[r][c]:
                                return
                            if type(cnt[cR][cC]) == int or side not in cnt[cR][cC]:
                                return
                            cnt[cR][cC].remove(side)
                            cR += tr
                            cC += tc
             
                    if side < 2:
                        #traverse vertical edge
                        traverseEdge(r + 1, c, 1, 0)
                        traverseEdge(r - 1, c, -1, 0)
                    else:
                        #traverse horizontal edge
                        traverseEdge(r, c + 1, 0, 1)
                        traverseEdge(r, c - 1, 0, -1)

        ans += area * sides
print(ans)