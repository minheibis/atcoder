import numpy as np
from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    arr = np.zeros((1000, 1000))
    for _ in range(N):
        lx, ly, rx, ry = nextInts()
        arr[ly:ry, lx:rx] += 1
    u, counts = np.unique(arr, return_counts=True)
    count_dict = defaultdict(int)
    for key, value in zip(u, counts):
        count_dict[int(key)] = value

    for i in range(1, N+1):
        print(count_dict[i])

solve()