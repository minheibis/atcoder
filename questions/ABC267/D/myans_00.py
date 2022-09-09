def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def calc_dot(v_a, v_b):
    v_dot = 0
    for x, y in zip(v_a,v_b):
        v_dot += x * y
    return v_dot

def print_dp(dp):
    for i, row in enumerate(dp):
        print(i, row)

def solve():
    N, M = nextInts()
    A = [0] + nextIntList()
    range_list = list(range(0, M+1))
    dp = [[0 for j in range(M+1)] for i in range(N+1)]

    # init
    for i in range(1, M+1):
        dp[i][i] = calc_dot(A[1:i+1], range_list[1:i+1])
    # print("init")
    # print(print_dp(dp))        

    for i in range(1, N+1):
        for j in range(1, min(i, M+1)):
            # print("i, j:", i, j)
            # print("dp[i-1][j]:", dp[i-1][j])
            # print("dp[i-1][j-1]:", dp[i-1][j-1])
            # print("dp[i-1][j-1]:", dp[i-1][j-1])
            # print("dp[i-1][j-1] + (A[i] * j):", dp[i-1][j-1] + (A[i] * j))
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-1] + (A[i] * j)
            )

    # print("last")
    # print(print_dp(dp))
    print(dp[N][M])

solve()