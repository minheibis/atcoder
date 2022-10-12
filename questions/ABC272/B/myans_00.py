from itertools import combinations
from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()

comb_deq = deque(combinations(range(1, N+1), 2))

for _ in range(M):
    x_list = nextIntList()
    k = x_list[0]
    x_list = x_list[1:]
    i_comb_deq = deque(combinations(x_list, 2))
    for i_comb in i_comb_deq:
        if i_comb in comb_deq:
            comb_deq.remove(i_comb)

if len(comb_deq) == 0:
    print("Yes")
else:
    print("No")