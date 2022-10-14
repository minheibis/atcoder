
# from start to all cells, write the minimum num of 移動する回数
# but have to change the minimum num if the path to there が更新された場合
# or 更新をさけるため、常に確実に最小になるように攻めていく。キューの上に置く、下に置くで管理できる？

import heapq

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

    que = []
    heapq.heappush(que, (0, (rs, cs), (0, 0)))
    while len(que):
        # print("que: ", que)
        now_change, now_cell, now_dir = heapq.heappop(que)
        if ans_maze[now_cell[0]][now_cell[1]] == "#":
            ans_maze[now_cell[0]][now_cell[1]] = now_change
        # print_maze(ans_maze)
        for next_dir in dir_list:
            next_cell = (now_cell[0] + next_dir[0], now_cell[1] + next_dir[1])
            if (0 <= next_cell[0] < H and
                0 <= next_cell[1] < W and
                ans_maze[next_cell[0]][next_cell[1]] == "#" and 
                maze[next_cell[0]][next_cell[1]] == "."):
                if now_dir == next_dir:
                    heapq.heappush(que, (now_change, next_cell, next_dir))
                else:
                    heapq.heappush(que, (now_change+1, next_cell, next_dir))
    # print_maze(ans_maze)
    print(ans_maze[rt][ct] - 1)

solve()