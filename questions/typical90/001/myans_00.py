def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def can_split(N, K, A, m):
    count = 0
    part_len = 0
    for i in range(1, N + 2):
        part_len += A[i] - A[i-1]
        if part_len >= m:
            part_len = 0
            count += 1
    if count >= (K + 1):
        return True
    else:
        return False

def solve():
    N, L = nextInts()
    K = nextInt()
    A = [0] + nextIntList() + [L]

    l = 0
    r = L
    while l < r - 1:
        # print(l, r)
        m = (l + r) >> 1
        if can_split(N, K, A, m):
            l = m
        else:
            r = m
    print(l)

solve()