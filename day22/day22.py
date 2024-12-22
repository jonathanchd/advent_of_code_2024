import sys
infile = sys.argv[1]
D = open(infile).read().strip()

lines = list(map(int, D.split('\n')))

ans = 0

def process(a):
    a = (a ^ (a * 64)) % 16777216
    a = (a ^ (a // 32)) % 16777216
    a = (a ^ (a * 2048)) % 16777216
    return a

for line in lines:
    for i in range(2000):
        line = process(line)
    ans += line

print(ans)