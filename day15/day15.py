import sys
infile = sys.argv[1]
D = open(infile).read().strip()

grid, moves = tuple(D.split('\n\n'))
grid = [[x for x in y] for y in grid.split('\n')]
moves = ''.join([x for x in moves.split('\n')])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

moveDict = {'^' : 2, '>' : 1, 'v' : 3, '<' : 0}

n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            grid[i][j] = '.'
            r, c = i, j

def printGrid(grid, r, c):
    grid[r][c] = '@'
    for row in grid:
        for char in row:
            print(char, end='')
        print()
    print()
    grid[r][c] = '.'

for move in moves:
    dir = moveDict[move]
    nr = r + dr[dir]
    nc = c + dc[dir]
    # print(move)
    if grid[nr][nc] == '#':
        # printGrid(grid, r, c)
        continue
    if grid[nr][nc] == '.':
        r, c = nr, nc
        # printGrid(grid, r, c)
        continue
    while grid[nr][nc] == 'O':
        nr += dr[dir]
        nc += dc[dir]
    if grid[nr][nc] == '#':
        # printGrid(grid, r, c)
        continue
    for i in range(2, max(abs(nr - r) + 1, abs(nc - c) + 1)):
        grid[r + dr[dir] * i][c + dc[dir] * i] = 'O'
    r += dr[dir]
    c += dc[dir]
    grid[r][c] = '.'
    # printGrid(grid, r, c)

grid[r][c] = '@'
ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] != 'O':
            continue
        ans += 100 * i + j

print(ans)