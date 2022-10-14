from collections import deque
# from start to all cells, write the minimum num of 移動する回数
# but have to change the minimum num if the path to there が更新された場合
# or 更新をさけるため、常に確実に最小になるように攻めていく。キューの上に置く、下に置くで管理できる？

def print_maze(maze):
    for maze_row in maze:
        print(*maze_row)

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
    ans_maze = [["#" for _ in range(W)] for _ in range(H)]
    
    # print_maze(maze)

    deq = deque()
    deq.appendleft(((rs, cs), (0, 0), 0))
    while deq:
        print("deq: ", deq)
        now_cell, now_dir, now_change = deq.popleft()
        if ans_maze[now_cell[0]][now_cell[1]] == "#": # 一度訪れたマスは更新しない
            ans_maze[now_cell[0]][now_cell[1]] = now_change
        print_maze(ans_maze)
        for next_dir in dir_list:
            next_cell = (now_cell[0] + next_dir[0], now_cell[1] + next_dir[1])
            if (0 <= next_cell[0] < H and
                0 <= next_cell[1] < W and
                ans_maze[next_cell[0]][next_cell[1]] == "#" and 
                maze[next_cell[0]][next_cell[1]] == "."):
                # 方向の確認は、next_dirと反対の方向のマスが、今のセルと同じかどうかで確認する。
                # ただし、before_cellがmapの中にない場合には、自動的に新しい方向になる。
                if now_cell == (rs, cs):
                    deq.append((next_cell, next_dir, now_change+1))
                else:
                    before_cell_1 = (now_cell[0] - next_dir[0], now_cell[1] - next_dir[1])
                    before_cell_2 = (now_cell[0] - 2 * next_dir[0], now_cell[1] - 2 * next_dir[1])
                    if ((before_cell_1[0] < 0 or H <= before_cell_1[0]) or
                        (before_cell_1[1] < 0 or W <= before_cell_1[1])):
                        deq.append((next_cell, next_dir, now_change+1))
                    elif ans_maze[before_cell_1[0]][before_cell_1[1]] != ans_maze[now_cell[0]][now_cell[1]]:
                        if ((before_cell_2[0] < 0 or H <= before_cell_2[0]) or
                            (before_cell_2[1] < 0 or W <= before_cell_2[1])):
                            deq.append((next_cell, next_dir, now_change))
                        elif ans_maze[before_cell_2[0]][before_cell_2[1]] != ans_maze[before_cell_1[0]][before_cell_1[1]]:
                            deq.append((next_cell, next_dir, now_change))
                        else:
                            deq.append((next_cell, next_dir, now_change+1))
                    else:
                        deq.appendleft((next_cell, next_dir, now_change))
    print("last")
    print_maze(ans_maze)
    print(ans_maze[rt][ct] - 1)

solve()