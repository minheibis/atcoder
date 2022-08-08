# https://atcoder.jp/contests/abc234/submissions/28433906


#写経
fac, inv, tmp = [1], [1], 1
p = 998244353
for x in range(1, 5001):
    tmp = tmp * x % p
    fac.append(tmp)
    inv.append(pow(tmp, p - 2, p))

def comb(a, b):
    if b > a: return 0
    x, y, z = fac[a], inv[b], inv[a-b]
    return x * y * z % p

s = input()
ls = len(s)
cnt = [0] * 26
for c in s: cnt[ord(c) - 97] += 1
s_cnt, tmp = [], 0
for i in range(26):
    tmp += cnt[i]
    s_cnt.append(tmp)

dp = [[0] * (ls + 1) for _ in range(26)]
for j in range(cnt[0]+1): dp[0][j] = 1

for i in range(1, 26):
    for j in range(s_cnt[i] + 1):
        for k in range(min(cnt[i], j) + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-k] * comb(j, k)) % p

print(sum(dp[-1][1:]) % p)


