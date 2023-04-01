from copy import copy

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

H, W = nextInts()
maze = []
for _ in range(H):
    maze.append(nextIntList())

ans_list = []

def search_next(now, now_set):
    now_i, now_j = now
    if now_i == W - 1 and now_j == H - 1:
        ans_list.append(1)
        return
    if now_i + 1 < W and maze[now_j][now_i + 1] not in now_set:
        next = (now_i + 1, now_j)
        next_set = copy(now_set)
        next_set.add(maze[now_j][now_i + 1])
        search_next(next, next_set)
    if now_j + 1 < H and maze[now_j + 1][now_i] not in now_set:
        next = (now_i, now_j + 1)
        next_set = copy(now_set)
        next_set.add(maze[now_j + 1][now_i])
        search_next(next, next_set)

now = (0, 0)
now_set = set()
now_set.add(maze[0][0])

search_next(now, now_set)
print(len(ans_list))