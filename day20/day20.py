import sys
from collections import deque
infile = sys.argv[1]
D = open(infile).read().strip()

grid = [[x for x in line] for line in D.split('\n')]
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E':
            er, ec = i, j

def good(r, c):
    return 0 <= r < n and 0 <= c < m

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dists = dict()
dists[(er, ec)] = 0

#originally i was trying to do some state tracking thing so this was a helper function to find the 
#distance of the original path
#i modified it so for each cell on the path it records the distance from the end
def findDists():
    dq = deque()
    dq.append((0, er, ec))
    while len(dq) != 0:
        dist, r, c = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not good(nr, nc) or grid[nr][nc] == '#' or (nr, nc) in dists:
                continue
            if grid[nr][nc] == 'S':
                dists[(nr, nc)] = dist + 1
                return dist + 1
            dists[(nr, nc)] = dist + 1
            dq.append((dist + 1, nr, nc))
    return -1

d = findDists()

#i realized cheats are constrained to cells on the path so i don't need to check every wall
#i figured this out while doing part 2 so literally the only dif between the two files is 2 vs 20 lol
#check every pair of cells on the path and see if it's reachable by a cheat
#if the manhattan distance <= 20 (or 2 for part 1), the cheat is doable
#time saved is abs(dists[a] - dists[b]) - manhatDist (time for cheat) 
ans = 0
dists = list(dists.items())
for i in range(len(dists)):
    for j in range(i + 1, len(dists)):
        (ar, ac), ad = dists[i]
        (br, bc), bd = dists[j]
        manhatDist = abs(ar - br) + abs(ac - bc)
        if manhatDist > 2:
            continue
        save = abs(ad - bd) - manhatDist
        if save >= 100:
            ans += 1

print(ans)

#i tried checking every wall and looked at its adjacent cells to find possible shortcuts but
#figured out the optimization above
"""
ans = 0
for r in range(1, n - 1):
    for c in range(1, m - 1):
        if grid[r][c] != '#':
            continue
        count = 4
        free = []
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if grid[nr][nc] == '#' or (nr, nc) not in dists:
                count -= 1
            else:
                free.append((nr, nc))
        for i in range(len(free)):
            for j in range(i + 1, len(free)):
                ar, ac = free[i]
                br, bc = free[j]
                save = abs(dists[free[i]] - dists[free[j]]) - 2
                if save >= 100:
                    ans += 1

print(ans)
"""

