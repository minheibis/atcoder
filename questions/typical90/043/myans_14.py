# REF1: https://github.com/E869120/kyopro_educational_90/blob/main/sol/043.cpp
# REF2: https://atcoder.jp/contests/typical90/submissions/35083989

from collections import deque
import numpy as np

d_list_x = [1, -1, 0, 0]
d_list_y = [0, 0, 1, -1]

INF = 1 << 32

def solve():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1
    maze = []
    for _ in range(H):
        maze.append(list(str(input())))
    deq = deque()
    ans_maze = np.full((H, W, 4), INF)
    for i in range(4):
        ans_maze[rs][cs][i] = 0
        deq.append([rs, cs, i])

    while deq:
        r_now, c_now, dr_now = deq.popleft()
        r_next = r_now + d_list_x[dr_now]
        c_next = c_now + d_list_y[dr_now]
        if (0 <= r_next < H and 
            0 <= c_next < W and
            maze[r_next][c_next] == "."):

            cnt_now = ans_maze[r_now][c_now][dr_now]
            for i in range(4):
                # その向きからいける次のマスの上下左右の方向を埋めていく。
                if i == dr_now and cnt_now < ans_maze[r_next][c_next][i]:
                    ans_maze[r_next][c_next][i] = cnt_now
                    deq.appendleft([r_next, c_next, i])
                else:
                    cnt_next = cnt_now + 1
                    if cnt_next < ans_maze[r_next][c_next][i]:
                        ans_maze[r_next][c_next][i] = cnt_next
                        deq.append([r_next, c_next, i])

    ans = INF
    for i in range(4):
        ans = min(ans, ans_maze[rt][ct][i])
    print(ans)

solve()