INF = (1 << 62) - 1

def main():
    def solve1():
        dp = [INF] * (N + 1)
        dp[1], dp[2] = A[1], A[1]
        for i in range(3, N + 1):
            dp[i] = min(dp[i - 2] + A[i - 1], dp[i - 1] + A[i])
        return dp[N]
    
    def solve2():
        dp = [INF] * (N + 1)
        dp[0], dp[1] = A[N], A[N]
        for i in range(2, N):
            dp[i] = min(dp[i - 2] + A[i - 1], dp[i - 1] + A[i])
        return dp[N - 1]
    
    N = int(input())
    A = [INF] + list(map(int, input().split()))
    print(min(solve1(), solve2()))

if __name__ == "__main__":
    main()