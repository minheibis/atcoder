import sys
import queue
h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]
q = queue.Queue()

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            q.put([i, j])
            visited[i][j] = 1

# 次のマスの探索のために使用する
dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while not q.empty():
    now = q.get()
    if c[now[0]][now[1]] == "g":
        print("Yes")
        sys.exit()
    for i in range(4):
        y = now[0] + dy_dx[i][0]
        x = now[1] + dy_dx[i][1]
        if 0 <= y < h and 0 <= x < w:
            if c[y][x] != "#" and visited[y][x] == 0:
                visited[y][x] = 1
                q.put([y, x])

print("No")