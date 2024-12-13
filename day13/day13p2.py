import sys
from sympy import symbols, Eq, solve
from sympy.core.numbers import Rational

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
    px += 10000000000000
    py += 10000000000000
    x, y = symbols('x y')
    eq1 = Eq(ax * x + bx * y, px)
    eq2 = Eq(ay * x + by * y, py)
    solution = solve((eq1, eq2), (x, y))
    if type(solution[x]) == Rational or type(solution[y]) == Rational:
        continue
    ans += 3 * solution[x] + solution[y]

print(ans)