# https://atcoder.jp/contests/typical90/submissions/35083989

INF = 1 << 32
mod = 10**9 + 7
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def ni(): return int(input())
def na(): return map(int, input().split())
def nl(): return list(map(int, input().split()))
def ns(): return input().strip()
def nsl(): return list(input().strip())

H, W = na()
sy, sx = na()
gy, gx = na()
field = [nsl() for _ in range(H)]

from collections import deque
que = deque()
que.append([sy-1, sx-1, 4])

dist = [[[INF] * W for _ in range(H)] for _ in range(4)]
for i in range(4):
    dist[i][sy-1][sx-1] = 0 

while que:
    y, x, d = que.popleft()

    for i, dydx in enumerate(dir):
        y2 = y + dydx[0]
        x2 = x + dydx[1]
        if not ((0 <= y2 < H) and (0 <= x2 < W)): continue
        if field[y2][x2] == "#": continue

        if d == 4:
            dist[i][y2][x2] = 0
            que.appendleft([y2, x2, i])
            continue

        elif i == d:
            if dist[i][y2][x2] > dist[i][y][x]:
                dist[i][y2][x2] = dist[i][y][x]
                for j in range(4):
                    if i == j: continue
                    dist[j][y2][x2] = min(dist[j][y2][x2], dist[i][y2][x2] + 1)
                que.appendleft([y2, x2, i])
        else:
            if dist[i][y2][x2] > dist[d][y][x] + 1:
                dist[i][y2][x2] = dist[d][y][x] + 1
                for j in range(4):
                    if i == j: continue
                    dist[j][y2][x2] = min(dist[j][y2][x2], dist[i][y2][x2] + 1)
                que.append([y2, x2, i])

ans = INF
for i in range(4):
    ans = min(dist[i][gy-1][gx-1], ans) 
print(ans)
