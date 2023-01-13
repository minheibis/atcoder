from collections import deque
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


n, k = nextInts()
a = deque(nextIntList())

for i in range(k):
    a.popleft()
    a.append(0)

print(*a)