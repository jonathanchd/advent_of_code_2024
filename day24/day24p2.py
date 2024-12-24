import sys
from collections import deque, defaultdict
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
adj = defaultdict(list)

for exp in exps:
    v, assign = exp.split(' -> ')
    if ' OR ' in v:
        a, b = v.split(' OR ')
        op = 'OR'
    elif 'AND' in v:
        a, b = v.split(' AND ')
        op = 'AND'
    else:
        a, b = v.split(' XOR ')
        op = 'XOR'
    dq.append((a, b, assign, op))
    adj[a].append((assign, op))
    adj[b].append((assign, op))
    
for key, lis in list(adj.items()):
    if key[0] != 'x' and key[0] != 'y':
        continue
    # print(f'trav {key}')
    adq = deque()
    seen = set()
    adq.append(str(key))
    while adq:
        cur = adq.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        for n, _ in adj[cur]:
            adq.append(n)
    zs = sorted([n for n in seen if n[0] == 'z'])
    print(f'{key} -> {zs[0]}')

