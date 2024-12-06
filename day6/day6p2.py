import sys
infile = sys.argv[1]
D = open(infile).read().strip()
lines = D.split('\n')

lines = [[a for a in line] for line in lines]

def good(r, c, lines):
    return r >= 0 and r < len(lines) and c >= 0 and c < len(lines[0])

def works(oR, oC, lines, r, c):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0
    visited = set()
    while True:
        nr = r + directions[dir][0]
        nc = c + directions[dir][1]
        if not good(nr, nc, lines):
            return False
        if lines[nr][nc] == '#':
            dir = (dir + 1) % 4
            continue

        if (nr, nc, dir) in visited:
            return True
        visited.add((nr, nc, dir))
        r, c = nr, nc

n = len(lines)
m = len(lines[0])
for i in range(n):
    found = False
    for j in range(m):
        if lines[i][j] == '^':
            r, c = i, j
            found = True
    if found:
        break

ans = 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == '#':
            continue
        prev = lines[i][j]
        lines[i][j] = "#"
        if works(i, j, lines, r, c):
            ans += 1
        lines[i][j] = prev

print(ans)