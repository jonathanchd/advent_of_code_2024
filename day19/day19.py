import sys

infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n\n')

towels = set([x.strip() for x in lines[0].split(',')])
designs = lines[1].split('\n')

ans = 0

for design in designs:
    n = len(design)
    doable = [False] * (n + 1)
    doable[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if doable[i] and design[i:j] in towels:
                doable[j] = True
    if doable[n]:
        ans += 1

print(ans)