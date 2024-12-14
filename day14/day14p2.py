import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

robots = []

for line in lines:
    line = line.split(' ')
    p = line[0][2:].split(',')
    v = line[1][2:].split(',')
    robots.append([int(p[0]), int(p[1]), int(v[0]), int(v[1])])

mnSafety = 1e9
index = -1
ans = []

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for i in range(10000):
    grid = [[' '] * 101 for _ in range(103)]
    for j, robot in enumerate(robots):
        x, y = robot[0], robot[1]
        x = (x + robot[2]) % 101
        y = (y + robot[3]) % 103
        robots[j] = [x, y, robot[2], robot[3]]
        grid[y][x] = '#'
    quads = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot[0], robot[1]
        if x == 50 or y == 51:
            continue
        if x > 50 and y > 51:
            quads[0] += 1
        if x < 50 and y > 51:
            quads[1] += 1
        if x < 50 and y < 51:
            quads[2] += 1
        if x > 50 and y < 51:
            quads[3] += 1
    mxDif = 0
    safety = quads[0] * quads[1] * quads[2] * quads[3]
    if safety < mnSafety:
        mnSafety = safety
        index = i
        ans = grid
    

print(index)
for line in ans:
    for char in line:
        print(char, end='')
    print()

print(mnSafety)

