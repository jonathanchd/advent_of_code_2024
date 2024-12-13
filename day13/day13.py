import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n\n')
ans = 0
for j, row in enumerate(lines):
    row = row.split('\n')
    row[0] = row[0][10:]
    row[1] = row[1][10:]
    row[2] = row[2][7:]
    row[0] = [x.strip() for x in row[0].split(',')]
    row[1] = [x.strip() for x in row[1].split(',')]
    row[2] = [x.strip() for x in row[2].split(',')]
    ax, ay = int(row[0][0][2:]), int(row[0][1][2:])
    bx, by = int(row[1][0][2:]), int(row[1][1][2:])
    px, py = int(row[2][0][2:]), int(row[2][1][2:])
    i = 1
    while i * ax <= px and i * ay <= py:
        remx = px - i * ax
        remy = py - i * ay
        if remy % by != 0 or remx % bx != 0 or (remx // bx) != (remy // by):
            i += 1
            continue
        ans += (3 * i) + (remx // bx)
        break

print(ans)