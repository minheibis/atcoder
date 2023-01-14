from itertools import combinations

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, K, D = nextInts()
A = nextIntList()

ans = -1
for c in combinations(A, K):
    tmp_ans = sum(c)
    if tmp_ans % D == 0:
        ans = max(tmp_ans, ans)

print(ans)