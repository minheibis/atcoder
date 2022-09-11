def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N, W = nextInts()
    wv_list = [[0, 0]]
    for _ in range(N):
        wv_list.append(nextIntList())

    dp = [[0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0]
        dp[i][0] = dp[i-1][1]
        for j in range(0, i):
            if dp[j][0] + wv_list[i][0] <= W:
                if dp[i-1][1] <= dp[j][1] + wv_list[i][1]:
                    dp[i][1] = dp[j][1] + wv_list[i][1]
                    dp[i][0] = dp[j][0] + wv_list[i][0]
    print(dp)
    print(dp[N][1])

solve()