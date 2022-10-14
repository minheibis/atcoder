from collections import deque
# from start to all cells, write the minimum num of 移動する回数
# but have to change the minimum num if the path to there が更新された場合
# or 更新をさけるため、常に確実に最小になるように攻めていく。キューの上に置く、下に置くで管理できる？

dir_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
    ans_maze = [[-1 for _ in range(W)] for _ in range(H)]

    deq = deque()
    deq.appendleft(((rs, cs), (0, 0), 0))
    while deq:
        now_cell, now_dir, now_change = deq.popleft()
        ans_maze[now_cell[0]][now_cell[1]] = now_change
        for next_dir in dir_list:
            next_cell = (now_cell[0] + next_dir[0], now_cell[1] + next_dir[1])
            if (0 <= next_cell[0] < H and
                0 <= next_cell[1] < W and
                ans_maze[next_cell[0]][next_cell[1]] == -1 and 
                maze[next_cell[0]][next_cell[1]] == "."):
                if now_dir == next_dir:
                    deq.appendleft((next_cell, next_dir, now_change))
                else:
                    deq.append((next_cell, next_dir, now_change+1))
    print(ans_maze[rt][ct] - 1)

solve()