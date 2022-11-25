def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

from collections import defaultdict

n, k = nextInts()
d = defaultdict(int)
for i in range(10**5 + 1):
    d[i] = 0

for _ in range(n):
    a, b = nextInts()
    d[a] += b

for key, value in d.items():
    k -= value
    if k <= 0:
        print(key)
        break