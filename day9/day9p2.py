import sys
infile = sys.argv[1]
line = open(infile).read().strip()


id = 0
inp = []
for i in range(len(line)):
    if i % 2 == 0:
        inp.append(('file', int(line[i]), id))
        id += 1
    elif int(line[i]) != 0:
        inp.append(('empty', int(line[i])))

ans = 0
r = len(inp) - 1
while r > 0:
    if inp[r][0] == 'empty':
        r -= 1
        continue
    idx = -1
    for i in range(r):
        if inp[i][0] == 'empty' and inp[i][1] >= inp[r][1]:
            print(inp[i][1], inp[r][1])
            idx = i
            break
    if idx == -1:
        r -= 1
        continue
    dif = inp[idx][1] - inp[r][1]
    inp[idx], inp[r] = inp[r], ('empty', inp[r][1])
    if dif > 0:
        if inp[idx + 1][0] == 'empty':
            inp[idx + 1] = ('empty', inp[idx + 1][1] + dif)
        else:
            inp.insert(idx + 1, ('empty', dif))
            r += 1
    r -= 1

i = 0
ans = 0
for thing in inp:
    if thing[0] == 'empty':
        i += thing[1]
    else:
        for j in range(thing[1]):
            ans += i * thing[2]
            i += 1

print(ans)