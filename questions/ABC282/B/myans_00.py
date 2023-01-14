from itertools import combinations

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
S = []
for _ in range(N):
    s = str(input())
    s_int = ""
    for c in s:
        if c == "o":
            s_int += "1"
        else:
            s_int += "0"
    S.append(int(s_int, 2))

all = combinations(S, 2)

ans = 0
yes = 2**M - 1
for x in all:
    if x[0] | x[1] == yes:
        ans += 1

print(ans)
