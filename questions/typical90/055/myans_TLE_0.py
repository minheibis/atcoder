# シンプルに考えると、nC5個の組み合わせを求めて、それぞれを7で割った余りを確認する。
from itertools import combinations
from math import prod

n, p, q = map(int, input().split())
a_list = list(map(int, input().split()))

comb_list = combinations(a_list, 5)
ans = 0
for comb in comb_list:
    if prod(comb) % p == q:
        ans += 1

print(ans)