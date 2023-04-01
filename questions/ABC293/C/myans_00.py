from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

H, W = nextInts()
maze = []
for _ in range(H):
    maze.append(nextIntList())

q = deque()
q.append((0, 0))
while q:
    node = q.popleft()
    i_now, j_now = node
    if maze[i_now + 1][j_now] not in

print(maze)