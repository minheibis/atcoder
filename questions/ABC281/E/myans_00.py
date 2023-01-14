from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M, K = nextInts()
A = nextIntList()

deq = deque()
#  最小が消える仕組み？
tmp_min = 
for i in range(N-M, N):
    deque.append(A[i])
    A[i] < 