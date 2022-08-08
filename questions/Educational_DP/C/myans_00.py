def solve():
    n = int(input())
    ps = []
    for _ in range(n):
        ps.append(list(map(int, input().split())))

    dp = [[0 for _ in range(3)] for _ in range(n)]
    for j in range(3):
        dp[0][j] = ps[0][j]

    for i in range(1, n):
        for j in range(3):
            ps_ij = []
            for k in range(3):
                if j != k:
                    ps_ij.append(
                        dp[i-1][k] + ps[i][j]
                    )
            dp[i][j] = max(ps_ij)

    print(max(dp[n-1]))

solve()