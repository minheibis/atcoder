def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
V = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = nextInts()
    V[a].append(b)
    V[b].append(a)

for i in range(1, N+1):
    v_len = len(V[i])
    print(v_len, *sorted(V[i]))