# シンプルに考えると、nC5個の組み合わせを求めて、それぞれをpで割った余りを確認する。
# 定数倍の処理が軽いため、これで通すことができる。らしい。

from itertools import combinations

n, p, q = map(int, input().split())
a_list = list(map(int, input().split()))
ans = 0

comb_list = combinations(a_list, 5)
for a, b, c, d, e in comb_list:
    if a%p * b%p * c%p * d%p * e%p == q:
        ans += 1

print(ans)