from queue import Queue
from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# continue until the candidate cells will be already visited

def solve():
    N, M = nextInts()
    
    steps = deque()
    for i in range(0, N):
        for j in range(i, N):
            dist = (i)**2 + (j)**2
            if M == dist:
                steps.append((i, j))
                if i != j:
                    steps.append((j, i))
    # print("steps:", steps)

    jump_ways = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    whole_map = [[-1 for _ in range(N)] for _ in range(N)]
    visited = deque()

    def print_map(whole_map):
        for i in range(N):
            print(*whole_map[i])

    def ij_to_num(i, j):
        num = (i - 1) * N + j
        return num

    visiting = Queue()
    visiting.put((1, 1, 0)) # i, j, jump_count

    while not visiting.empty():
        pos = visiting.get()
        visited.append(ij_to_num(pos[0], pos[1]))
        whole_map[pos[0] - 1][pos[1] - 1] = pos[2]
        # print("pos, jump_count: ", pos)
        # print("visited: ", visited)
        # print_map(whole_map)

        for step in steps:
            for jump_way in jump_ways:
                next_i = pos[0] + step[0] * jump_way[0]
                next_j = pos[1] + step[1] * jump_way[1]
                if ((next_i > 0 and next_i <= N)
                 and (next_j > 0 and next_j <= N)
                 and (ij_to_num(next_i, next_j) not in visited)
                ):
                    next_pos = (
                        pos[0] + step[0] * jump_way[0],
                        pos[1] + step[1] * jump_way[1],
                        pos[2] + 1
                    )
                    visiting.put(next_pos)

    print_map(whole_map)
    


solve()
