from copy import deepcopy
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


N, P, Q, R, S = nextInts()
A = nextIntList()

tmp = deepcopy(A[P-1:Q])
A[P-1:Q] = A[R-1:S]
A[R-1:S] = tmp
print(*A)

