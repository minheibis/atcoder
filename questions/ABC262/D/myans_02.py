from itertools import combinations

MOD = 998244353

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
a_list = nextIntList()
a_list = [:n // 2]

ans = 0
for i in range(1, n+1):
    all_comb = combinations(a_list, i)
    for comb in all_comb:
        if sum(comb) % i == 0:
            ans += 1
            ans %= MOD

print(ans)