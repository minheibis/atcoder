INF = 10**9 + 1

def solve():
    n, k = map(int, input().split())   
    hs = list(map(int, input().split()))

    dp = [0 for _ in range(n)]
    # print("dp:", dp)
    for i in range(1, n):
        cost = INF
        range_min = max(0, i - k)
        for j in range(range_min, i):
            # print("i, j:", i, j)
            # print("dp[j] + abs(hs[i] - hs[j]): ", dp[j] + abs(hs[i] - hs[j]))
            cost = min(cost, dp[j] + abs(hs[i] - hs[j]))
        dp[i] = cost
    # print(dp)
    print(dp[n-1])

solve()