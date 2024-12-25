import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = [x.split('\n') for x in D.split('\n\n')]

locks = [x for x in lines if x[0][0] == '#']
keys = [x for x in lines if x[0][0] == '.']

locks = [tuple([sum(1 for row in lock if row[i] == '#') for i in range(5)]) for lock in locks]
keys = [tuple([sum(1 for row in key if row[i] == '#') for i in range(5)]) for key in keys]

ans = 0

for lock in locks:
    for key in keys:
        sm = sum(1 for i in range(5) if lock[i] + key[i] <= 7)
        if sm == 5:
            ans += 1

print(ans)