from collections import deque

d_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solve():
    # 入力
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
    ans_maze = [["#" for _ in range(W)] for _ in range(H)]
    ans_maze[rs][cs] = -1 # 開始地点
    deq = deque()
    deq.append((rs, cs))
    while deq:
        r_now, c_now = deq.popleft()
        cnt_next = ans_maze[r_now][c_now] + 1
        for d in d_list:
            r_next, c_next = r_now, c_now
            while True:
                r_next += d[0]
                c_next += d[1]
                if (0 <= r_next < H and 
                    0 <= c_next < W and
                    maze[r_next][c_next] == "." and
                    (ans_maze[r_next][c_next] == "#" or ans_maze[r_next][c_next] == cnt_next)
                ):
                    ans_maze[r_next][c_next] = cnt_next
                    deq.append((r_next, c_next))
                else:
                    break
    print(ans_maze[rt][ct])
            
solve()