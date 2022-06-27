import sys
h, w = map(int, input().split())
c = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j # スタート
        elif c[i][j] == "g":
            gx, gy = i, j # ゴール

stack = [[sx, sy]]
visited = [[0 for i in range(w)] for j in range(h)]
visited[sx][sy] = 1

# 次のマスの探索のために使用する
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while stack:
    x, y = stack.pop() # 要素を取り出す
    for i in range(4):
        nx, ny = x + dx_dy[i][0], y+dx_dy[i][1] # 探索する位置
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and c[nx][ny] != "#":
            visited[nx][ny] = 1
            stack.append([nx, ny]) # stackに追加
        if visited[gx][gy] == 1:
            print("Yes")
            sys.exit()

print("No")