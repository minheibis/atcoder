from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# continue until the candidate cells will be already visited


def solve():
    N, M = nextInts()
    
    steps = deque()
    for i in range(0, N):
        for j in range(0, N):
            dist = (i)**2 + (j)**2
            if M == dist:
                steps.append((i, j))
    print("steps:", steps)

    jump_ways = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    whole_map = [[-1 for _ in range(N)] for _ in range(N)]
    visited = deque()

    def print_map(whole_map):
        for i in range(N):
            print(whole_map[i])

    def ij_to_num(pos):
        i, j = pos[0], pos[1]
        num = (i - 1) * N + j
        return num

    def jump_func(pos, jump_count):
        visited.append(ij_to_num(pos))
        whole_map[pos[0] - 1][pos[1] - 1] = jump_count

        print("pos, jump_count: ", pos, jump_count)
        print("visited: ", visited)
        print_map(whole_map)

        all_visited = True
        for step in steps:
            for jump_way in jump_ways:
                print("jump_way: ", jump_way)
                next_pos = [
                    pos[0] + step[0] * jump_way[0],
                    pos[1] + step[1] * jump_way[1]
                ]
                if ((next_pos[0] > 0 and next_pos[0] <= N)
                 and (next_pos[1] > 0 and next_pos[1] <= N)
                 and ij_to_num(next_pos) not in visited
                ):
                    all_visited = False
                    jump_func(next_pos, jump_count+1)
        if all_visited == True:
            return
    
    jump_func([1, 1], 0)
    print_map(whole_map)
    


solve()
