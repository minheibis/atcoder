from cmath import cos


def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
hs = nextIntList()
costs = [0 for _ in range(n)]
costs[0] = 0
costs[1] = abs(hs[1] - hs[0])

for i in range(2, n):
    costs[i] = min(
        costs[i-1] + abs(hs[i] - hs[i-1]),
        costs[i-2] + abs(hs[i] - hs[i-2])
    )

print(costs[n-1])