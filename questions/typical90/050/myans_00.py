MOD = 10**9 + 7
n, l = map(int, input().split())

ans = 0

dp = [0 for _ in range(n)]
for i in range(0, n):
    if i < l - 1:
        way = 1
    elif i == l - 1:
        way = 2
    elif i >= l - 1:
        way = dp[i - 1] + dp[i - l]
    way %= MOD
    dp[i] = way
    # print("i, way: ", i, way)

print(dp[n-1])