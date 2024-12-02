import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

def good(lis):
    if lis != sorted(lis) and lis != sorted(lis, reverse=True):
        return False
    for i in range(len(lis) - 1):
        dif = abs(lis[i] - lis[i + 1])
        if not 1 <= dif <= 3:
            return False
    return True

d1 = 0
d2 = 0
for line in lines:
    line = list(map(int, line.split()))
    if good(line):
        d1 += 1
    
    yay = False
    for i in range(len(line)):
        if good(line[:i] + line[i + 1:]):
            yay = True
            break
    if yay:
        d2 += 1

print(d1, d2)