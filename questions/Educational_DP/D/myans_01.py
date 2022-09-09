def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N, W = nextInts()
    wv_list = [[0, 0]]
    for _ in range(N):
        wv_list.append(nextIntList())

    dp = [[0 for _ in range(W + 1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(0, W+1):
            if j - wv_list[i][0] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - wv_list[i][0]] + wv_list[i][1])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    print(dp[N][W])

solve()