import sys
from functools import cache
infile = sys.argv[1]

line = open(infile).read().strip().split(' ')

@cache
def count(n, a):
    if a == 75:
        return 1
    if n == '0':
        return count('1', a + 1)
    if len(n) % 2 == 0:
        return (count(n[:len(n) // 2], a + 1) + count(str(int(n[len(n) // 2:])), a + 1))
    return count(str(int(n) * 2024), a + 1)

ans = sum([count(x, 0) for x in line])

print(ans)