from collections import deque

N, Q = map(int, input().split())
S = str(input())
S_len = len(S)

a = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        a -= x
    else:
        print(S[(a+x-1) % S_len])