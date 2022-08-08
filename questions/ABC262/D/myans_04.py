# https://atcoder.jp/contests/abc262/submissions/33720982

import re


MOD = 998244353
N = int(input())
A = [*map(int, input().split())]

def solve(n):
    dp = [[0 for _ in range(n)] for _ in range(n+1)]
    dp[0][0] = 1
    for ai in A:
        for j in range(n, 0, -1): # 選ぶ個数　逆から回す(aiを使う場合の結果は更新したくないので、先に使う場合を更新)
            for k in range(n): # 余り
                dp[j][k] += dp[j-1][(k - ai) % n] # 足した結果あまりがkになるもの。上を逆から回していることで、この時点で、j-1は未更新なので、利用可能になる。
#                print("j, k: ", j, k)
#                print(dp)
    return dp[n][0]

print(sum(solve(n) for n in range(1, N+1)) % MOD)