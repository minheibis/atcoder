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
    dir_maze = [[{"change": -1, "dir_list": []} for _ in range(W)] for _ in range(H)] # 方向の管理
    dir_maze[rs][cs]["change"] = 0
    dir_maze[rs][cs]["dir_list"].append((0, 0))
    
    deq = deque()
    deq.appendleft((rs, cs))
    while deq:
        # print("deq: ", deq)
        now_cell = deq.popleft()
        now_change = dir_maze[now_cell[0]][now_cell[1]]["change"]
        now_dir_list = dir_maze[now_cell[0]][now_cell[1]]["dir_list"]
        if ans_maze[now_cell[0]][now_cell[1]] == "#":
            ans_maze[now_cell[0]][now_cell[1]] = now_change
        # print_maze(ans_maze)
        # print_maze(dir_maze)
        for next_dir in dir_list:
            next_cell = (now_cell[0] + next_dir[0], now_cell[1] + next_dir[1])
            if (0 <= next_cell[0] < H and
                0 <= next_cell[1] < W and
                ans_maze[next_cell[0]][next_cell[1]] == "#" and 
                maze[next_cell[0]][next_cell[1]] == "."):
                if next_dir in now_dir_list:
                    next_change = now_change
                else:
                    next_change = now_change + 1
                deq.append(next_cell)
                if dir_maze[next_cell[0]][next_cell[1]]["change"] == -1:
                    dir_maze[next_cell[0]][next_cell[1]]["change"] = next_change
                    dir_maze[next_cell[0]][next_cell[1]]["dir_list"].append(next_dir)
                elif dir_maze[next_cell[0]][next_cell[1]]["change"] == next_change:
                    dir_maze[next_cell[0]][next_cell[1]]["dir_list"].append(next_dir)
                elif dir_maze[next_cell[0]][next_cell[1]]["change"] > next_change:
                    dir_maze[next_cell[0]][next_cell[1]]["change"] = next_change
                    dir_maze[next_cell[0]][next_cell[1]]["dir_list"] = [next_dir]
    # print("last")
    # print_maze(ans_maze)
    print(ans_maze[rt][ct] - 1)

solve()