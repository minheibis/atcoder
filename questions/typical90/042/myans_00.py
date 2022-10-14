def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 10**9 + 7

def solve():
    K = nextInt()
    if K % 9 != 0:
        print(0)
    else:
        dp = [0 for _ in range(K + 1)]
        dp[0] = 1
        for i in range(1, K + 1):
            tmp_max = min(i + 1, 10)
            for j in range(1, tmp_max):
                dp[i] += dp[i - j]
                dp[i] %= MOD
        # print(dp)
        print(dp[K])

solve()