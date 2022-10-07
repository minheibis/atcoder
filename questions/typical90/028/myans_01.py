# https://twitter.com/e869120/status/1388262816101007363/photo/1

from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    arr = [[0 for _ in range(1001)] for _ in range(1001)]

    for _ in range(N):
        lx, ly, rx, ry = nextInts()
        arr[ly][lx] += 1
        arr[ly][rx] -= 1
        arr[ry][lx] -= 1
        arr[ry][rx] += 1
    
    for i in range(0, 1001):
        for j in range(1, 1001):
            arr[i][j] += arr[i][j - 1]
    for i in range(1, 1001):
        for j in range(0, 1001):
            arr[i][j] += arr[i - 1][j]

    # count
    count_dict = defaultdict(int)
    for i in range(1000):   
        for j in range(1000):
            if arr[i][j] >= 1:
                count_dict[arr[i][j]] += 1
                
    for i in range(1, N+1):
        print(count_dict[i])

solve()