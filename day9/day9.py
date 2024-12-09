import sys
infile = sys.argv[1]
line = open(infile).read().strip()


id = 0
inp = []
for i in range(len(line)):
    if i % 2 == 0:
        for i in range(int(line[i])):
            inp.append(id)
        id += 1
    else:
        for i in range(int(line[i])):
            inp.append('.')
ans = 0
n = len(inp)
i, ptr = 0, n - 1
while i < ptr:
    if type(inp[i]) != str:
        i += 1
        continue
    while ptr > i and type(inp[ptr]) == str:
        ptr -= 1
    if ptr == i:
        break
    inp[i], inp[ptr] = inp[ptr], inp[i]
    i += 1
    ptr -= 1

ans = 0
for i in range(len(inp)):
    if type(inp[i]) != str:
        ans += i * inp[i]
print(ans)