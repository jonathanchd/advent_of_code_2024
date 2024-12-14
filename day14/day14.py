import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

robots = []

for line in lines:
    line = line.split(' ')
    p = line[0][2:].split(',')
    v = line[1][2:].split(',')
    robots.append((int(p[0]), int(p[1]), int(v[0]), int(v[1])))

finalPos = []

for robot in robots:
    x = robot[0] + 100 * robot[2]
    y = robot[1] + 100 * robot[3]
    x = x % 101
    y = y % 103
    finalPos.append((x, y))

quads = [0, 0, 0, 0]

for x, y in finalPos:
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

print(quads[0] * quads[1] * quads[2] * quads[3])