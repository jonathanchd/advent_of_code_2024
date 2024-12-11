import sys
from functools import cache
infile = sys.argv[1]

line = open(infile).read().strip().split(' ')

# line = [int(x) for x in D]
print(line)

for i in range(75):
    nw = []
    print(i)
    for x in line:
        if x == '0':
            nw.append('1')
        elif len(x) % 2 == 0:
            nw.append(x[:len(x) // 2])
            nw.append(str(int(x[len(x)//2:])))
        else:
            nw.append(str(int(x) * 2024))
    line = nw
    # print(line)

print(len(line))