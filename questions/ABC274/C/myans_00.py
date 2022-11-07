from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    a_list = nextIntList()

    am_list = [0 for _ in range(2 * N + 1)]
    for i, a in enumerate(a_list):
        am_list[i * 2 + 1] = am_list[a-1] + 1
        am_list[i * 2 + 2] = am_list[a-1] + 1

    print(*am_list)

solve()