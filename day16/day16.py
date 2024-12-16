import sys
import heapq
infile = sys.argv[1]
D = open(infile).read().strip()

def good(r, c):
    global n, m
    return 0 <= r < n and 0 <= c < m

lines = D.split('\n')

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
        ans = dist
        break
    nr, nc = r + dr[dir], c + dc[dir]
    # move forward if we can
    if good(nr, nc) and lines[nr][nc] != '#':
        heapq.heappush(pq, (dist + 1, dir, nr, nc))
    #try turning to both sides
    heapq.heappush(pq, (dist + 1000, (dir + 1) % 4, r, c))
    heapq.heappush(pq, (dist + 1000, (dir + 3) % 4, r, c))
print(ans)
