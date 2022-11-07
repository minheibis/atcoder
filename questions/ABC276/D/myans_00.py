def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    A = nextIntList()

    ans = 0
    now = A[0]
    for i in range(1, N):
        next = A[i]
        if now == next:
            continue
        else:
            if now % 2 == 0:



solve()