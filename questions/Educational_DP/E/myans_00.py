INF = 10**5 + 1

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N, W = nextInts()
    w_list = [0]
    v_list = [0]
    for _ in range(N):
        w, v = nextInts()
        w_list.append(w)
        v_list.append(v)

    dp = [[pow(10,9)+1 for _ in range(INF)] for _ in range(N + 1)]

    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(0, INF):
            if j - v_list[i] >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v_list[i]] + w_list[i])
            else:
                dp[i][j] = dp[i-1][j]
    # あるvを作るのに必要な最小の重さの合計を求めていく
    ans = INF - 1
    while(dp[N][ans] > W):
        ans -= 1
    print(ans)
    # そのうえで、W以下にした際の、最大のvを求める。
solve()