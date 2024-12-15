import sys
infile = sys.argv[1]
D = open(infile).read().strip()

def printGrid(grid, r, c):
    grid[r][c] = '@'
    for row in grid:
        for char in row:
            print(char, end='')
        print()
    print()
    grid[r][c] = '.'

grid, moves = tuple(D.split('\n\n'))
grid = [[x for x in y] for y in grid.split('\n')]
moves = ''.join([x for x in moves.split('\n')])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

moveDict = {'^' : 2, '>' : 1, 'v' : 3, '<' : 0}

newGrid = []
for row in grid:
    newRow = []
    for c in row:
        if c == '#':
            newRow.append('#')
            newRow.append('#')
        elif c == 'O':
            newRow.append('[')
            newRow.append(']')
        elif c == '.':
            newRow.append('.')
            newRow.append('.')
        elif c == '@':
            newRow.append('@')
            newRow.append('.')
    newGrid.append(newRow)

grid = newGrid

n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            grid[i][j] = '.'
            r, c = i, j

printGrid(grid, r, c)

def pushHorizontal(dir):
    global grid, r, c
    nr, nc = r + dr[dir], c + dc[dir]
    while grid[nr][nc] == '[' or grid[nr][nc] == ']':
        nr += dr[dir] * 2
        nc += dc[dir] * 2
    if grid[nr][nc] == '#':
        return
    while nc != c:
        grid[nr][nc] = grid[nr][nc - dc[dir]]
        nc -= dc[dir]
    grid[r][c] = '.'
    r += dr[dir]
    c += dc[dir]

#assume nr, nc are the '[' side of the box
#returns true of we can make the push
def checkok(nr, nc, dir):
    global grid
    # print(f'check {nr, nc} {grid[nr][nc]}')
    nextr = nr + dr[dir]
    #blocked
    if grid[nextr][nc] == '#' or grid[nextr][nc + 1] == '#':
        return False
    #open space
    if grid[nextr][nc] == '.' and grid[nextr][nc + 1] == '.':
        return True
    # print(grid[nextr][nc + 1])
    if grid[nextr][nc] == '[':
        # print(1)
        return checkok(nextr, nc, dir)
    elif grid[nextr][nc] == ']' and grid[nextr][nc + 1] == '[':
        # print(2)
        return checkok(nextr, nc - 1, dir) and checkok(nextr, nc + 1, dir)
    elif grid[nextr][nc + 1] == '[':
        # print(3)
        return checkok(nextr, nc + 1, dir)
    elif grid[nextr][nc] == ']':
        # print(4)
        return checkok(nextr, nc - 1, dir)
    


def recursivePush(nr, nc, dir):
    global grid
    # print(f'pushing {nr} {nc}')
    nextr = nr + dr[dir]
    #open space (no more recursive calls yay)
    if grid[nextr][nc] == '.' and grid[nextr][nc + 1] == '.':
        # print('open')
        grid[nr][nc] = '.'
        grid[nr][nc + 1] = '.'
        grid[nextr][nc] = '['
        grid[nextr][nc + 1] = ']'
        # printGrid(grid, 0, 0)
        return
    
    if grid[nextr][nc] == '[':
        recursivePush(nextr, nc, dir)
    elif grid[nextr][nc] == ']' and grid[nextr][nc + 1] == '[':
        recursivePush(nextr, nc - 1, dir)
        recursivePush(nextr, nc + 1, dir)
    elif grid[nextr][nc + 1] == '[':
        recursivePush(nextr, nc + 1, dir)
    elif grid[nextr][nc] == ']':
        recursivePush(nextr, nc - 1, dir)
    
    grid[nr][nc] = '.'
    grid[nr][nc + 1] = '.'
    grid[nextr][nc] = '['
    grid[nextr][nc + 1] = ']'
    

def pushVertical(dir):
    global grid, r, c
    nr, nc = r + dr[dir], c + dc[dir]
    if grid[nr][nc] == '[':
        # print(f'check {grid[nr][nc]}')
        res = checkok(nr, nc, dir)
    else:
        # print(f'check {grid[nr][nc - 1]}')
        res = checkok(nr, nc - 1, dir)
    if not res:
        return
    if grid[nr][nc] == '[':
        recursivePush(nr, nc, dir)
    else:
        recursivePush(nr, nc - 1, dir)
    r += dr[dir]
    c += dc[dir]


for i, move in enumerate(moves):
    dir = moveDict[move]
    nr = r + dr[dir]
    nc = c + dc[dir]
    # print(i, move)
    if grid[nr][nc] == '#':
        # printGrid(grid, r, c)
        continue
    if grid[nr][nc] == '.':
        r, c = nr, nc
        # printGrid(grid, r, c)
        continue
    if dir < 2:
        pushHorizontal(dir)
    else:
        pushVertical(dir)
    # printGrid(grid, r, c)

grid[r][c] = '@'
printGrid(grid, r, c)
ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] != '[':
            continue
        ans += 100 * i + j

print(ans)