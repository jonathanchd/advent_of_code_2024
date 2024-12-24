import sys
from collections import deque
infile = sys.argv[1]
D = open(infile).read().strip()

inits, exps = D.split('\n\n')

inits = inits.split('\n')
vars = dict()
for init in inits:
    var, val = init.split(': ')
    vars[var] = int(val)

exps = exps.split('\n')

dq = deque()


for exp in exps:
    v, assign = exp.split(' -> ')
    if ' OR ' in v:
        a, b = v.split(' OR ')
        dq.append((a, b, assign, 'OR'))
    elif 'AND' in v:
        a, b = v.split(' AND ')
        dq.append((a, b, assign, 'AND'))
    else:
        a, b = v.split(' XOR ')
        dq.append((a, b, assign, 'XOR'))

while dq:
    a, b, assign, op = dq.popleft()
    if a not in vars or b not in vars:
        dq.append((a, b, assign, op))
        continue
    if op == 'OR':
        vars[assign] = vars[a] | vars[b]
    elif op == 'AND':
        vars[assign] = vars[a] & vars[b]
    else:  
        vars[assign] = vars[a] ^ vars[b]
    
ans = sorted([(var, val) for var, val in vars.items() if var[0] == 'z' ])
ans = ''.join([str(val) for var, val in ans])[::-1]
print(int(ans, 2))
