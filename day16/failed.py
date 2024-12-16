#tried using dfs/bfs but was too slow
#i realized i could use dijkstras + marking previous states from a given current state of (pos, dir)
import sys
import heapq
from collections import deque
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

best = set()
path = set()
seen = set()

def search(dist, dir, r, c):
    global shortest, best, path, seen
    if r == er and c == ec:
        # copy = lines
        for br, bc, dir in path:
            # copy[br][bc] = 'O'
            best.add((br, bc))
        # path.remove((r, c, dir))
        # print("best")
        # for row in copy:
        #     for c in row:
        #         print(c, end = '')
        #     print()
        return
    # print(r, c)
    if (r, c, dir) in seen:
        # print(r, c, dir, "SEEN")
        return
    seen.add((r, c, dir))
    if dist > shortest:
        seen.remove((r, c, dir))
        return
    # print(r, c, dir, dist)
    path.add((r, c, dir))
    
    
    nr, nc = r + dr[dir], c + dc[dir]
    # move forward if we can
    if good(nr, nc) and lines[nr][nc] != '#':
        search(dist + 1, dir, nr, nc)
    
    search(dist + 1000, (dir + 1) % 4, r, c)
    search(dist + 1000, (dir + 3) % 4, r, c)
    seen.remove((r, c, dir))
    path.remove((r, c, dir))



search(0, 0, sr, sc)
    
print(len(best))

for r, c in best:
    lines[r][c] = 'O'

for row in lines:
    for c in row:
        print(c, end = '')
    print()