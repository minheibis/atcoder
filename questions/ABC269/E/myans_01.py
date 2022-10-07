# とにかく交互に2分探索

from sys import exit

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
u = 1
b = N
l = 1
r = N
while b > u:
    mub = (u + b + 1) // 2
    print("?", u, mub - 1, 1, N)
    T = nextInt()
    if T == -1:
        exit()
    if T != (mub - u + 1):
        b = mub
    else:
        u = mub + 1

while r > l:
    mlr = (l + r + 1) // 2
    print("?", 1, N, l, mlr)
    T = nextInt()
    if T == -1:
        exit()
    if T != (mlr - l + 1):
        r = mlr
    else:
        l = mlr + 1

print("!", u, l)