# とにかく交互に2分探索
from math import ceil

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
u = 1
b = N
l = 1
r = N
while b > u or r > l:
    # test_row
    if b != u:
        mub = u + ((b - u) >> 1)
        print("?", u, mub, 1, N)
        T = nextInt()
        if T != (mub - u + 1):
            b = mub
        else:
            u = mub + 1

    # test_col
    if l != r:
        mlr = l + ((r - l) >> 1)
        print("?", 1, N, l, mlr)
        T = nextInt()
        if T != (mlr - l + 1):
            r = mlr
        else:
            l = mlr + 1

print("!", u, l)