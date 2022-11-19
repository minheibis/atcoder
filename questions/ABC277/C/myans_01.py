def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

from collections import deque

N = nextInt()
V = [[] for _ in range(N)]
for i in range(N):
    A, B = nextInts()
    V[A-1].append(B-1)
    V[B-1].append(A-1)

visited = set([0])
deq = deque()
deq.append(0)

ans = 0
while deq:
    now = deq.pop()
    ans = max(ans, now)

    next_list = V[now]
    for next in next_list:
        if next not in visited:
            deq.append(next)
            visited.add(next)
    
print(ans + 1)