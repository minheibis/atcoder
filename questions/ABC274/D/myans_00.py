from collections import deque
from itertools import accumulate

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# manhattennで枝刈り

def calc_man(x, y, x_next, y_next):
    return abs(x-x_next) + abs(y-y_next)

def solve():
    N, x, y = nextInts()
    a_list = nextIntList()

    deq = deque()
    deq.append((a_list[0], 0, 1, 0)) # pos_x, pos_y, rem_dir, a

    accum_list = list(reversed(list(accumulate(reversed(a_list)))))

    while deq:
        print(deq)
        now_x, now_y, now_dir, now_a = deq.popleft()
        new_a = now_a + 1
        if new_a < N:
            a_val = a_list[new_a]
            for i in range(4):
                if i == now_dir:
                    continue
                new_dir = i
                new_x, new_y = now_x, now_y
                if i == 0:
                    if now_dir == 1:
                        continue
                    new_x += a_val
                elif i == 1:
                    if now_dir == 0:
                        continue
                    new_x -= a_val
                elif i == 2:
                    if now_dir == 3:
                        continue
                    new_y += a_val
                elif i == 3:
                    if now_dir == 2:
                        continue
                    new_y -= a_val
                # print("new_a, new_x, new_y: ", new_a, new_x, new_y)
                if new_a == N - 1 and new_x == x and new_y == y:
                    print("Yes")
                    return
                elif new_a + 1 < N:
                    deq.append((new_x, new_y, new_dir, new_a)) # pos_x, pos_y, rem_dir, a

    print("No")
    return

solve()