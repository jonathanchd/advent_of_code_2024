import sys
import heapq
from collections import defaultdict
infile = sys.argv[1]
D = open(infile).read().strip()

def good(r, c):
    global n, m
    return 0 <= r < n and 0 <= c < m

lines = D.split('\n')
lines = [[x for x in line] for line in lines]

n, m = len(lines), len(lines[0])

for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            sr, sc = i, j
        if lines[i][j] == 'E':
            er, ec = i, j

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = 0 # start east
pq = [(0, dir, sr, sc)]
heapq.heapify(pq)
seen = set()
while len(pq) > 0:
    dist, dir, r, c = heapq.heappop(pq)
    if (r, c, dir) in seen:
        continue
    seen.add((r, c, dir))
    if r == er and c == ec:
        shortest = dist
        break
    nr, nc = r + dr[dir], c + dc[dir]
    # move forward if we can
    if good(nr, nc) and lines[nr][nc] != '#':
        heapq.heappush(pq, (dist + 1, dir, nr, nc))
    #try turning to both sides
    heapq.heappush(pq, (dist + 1000, (dir + 1) % 4, r, c))
    heapq.heappush(pq, (dist + 1000, (dir + 3) % 4, r, c))


bestDist = defaultdict(lambda: 1e9)
#keep track of previous states for each state
prev = defaultdict(lambda: [])

pq = [(0, 0, sr, sc)]
heapq.heapify(pq)
while len(pq) > 0:
    dist, dir, r, c = heapq.heappop(pq)
    if dist > shortest:
        continue
    if r == er and c == ec:
        continue
    state = (r, c, dir)
    for nr, nc, ndir, ndist in [(r + dr[dir], c + dc[dir], dir, dist + 1),
                                (r, c, (dir + 1) % 4, dist + 1000),
                                (r, c, (dir + 3) % 4, dist + 1000)]: 
        newState = (nr, nc, ndir)
        if good(nr, nc) and lines[nr][nc] != '#':
            #if new best dist found, reset the list and search again
            if newState not in bestDist or bestDist[newState] > ndist:
                bestDist[newState] = ndist
                prev[newState] = [(state)]
                heapq.heappush(pq, (ndist, ndir, nr, nc))
            #otherwise just add the cell to the list
            elif bestDist[newState] == ndist:
                prev[newState].append(state)


best = set()
#backtrack from the end to find every cell that belongs to a best path
def resolve(r, c, dir):
    # global lines
    # lines[r][c] = 'O'
    global best
    best.add((r, c))
    if r == sr and c == sc:
        return
    for nr, nc, ndir in prev[(r, c, dir)]:
            resolve(nr, nc, ndir)

resolve(er, ec, 0)
resolve(er, ec, 1)
resolve(er, ec, 2)
resolve(er, ec, 3)

print(len(best))