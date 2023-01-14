from functools import lru_cache

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
A = nextIntList()
B = [i + 1 for i in range(N)]
B_i = [i + 1 for i in range(N)]

# order(N)
logs = []
for a in A:
    k = B[a - 1]
    l = B[a]
    logs.append((k, l))
    B[a - 1], B[a] = B[a], B[a - 1]
    B_i[k - 1], B_i[l - 1] = B_i[l - 1], B_i[k - 1]


ans_base = B_i[1 - 1]
for i, log in enumerate(logs):
    k, l = log
    ans = ans_base
    if k == 1:
        ans = B_i[l - 1]
    elif l == 1:
        ans = B_i[k - 1]

    print(ans)