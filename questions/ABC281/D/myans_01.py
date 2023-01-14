from itertools import combinations

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, K, D = nextInts()
A = nextIntList()

def print_dp(dp):
    for n in range(N):
        print(n, ":", dp[n])

dp = [[[-1 for d in range(D)] for k in range(K)] for n in range(N)]

for n, a in enumerate(A):
    a_rem = a % D
    if n == 0:
        dp[n][0][a_rem] = a
        # print("dp[n][0] first: ", dp[n][0])
    else:
        dp[n][0][a_rem] = max(dp[n-1][0][a % D], a)
        # print("dp[n][0]: ", dp[n][0])
        for k in range(K):
            for d in range(D):          
                if k == 0:
                    dp[n][k][d] = max(dp[n][k][d], dp[n-1][k][d])
                else:
                    a_rem_rev = (d - a_rem) % D
                    if dp[n-1][k-1][a_rem_rev] != -1:
                        dp[n][k][d] = max(dp[n][k][d], dp[n-1][k][d], dp[n-1][k-1][a_rem_rev] + a)
                    else:
                        dp[n][k][d] = max(dp[n][k][d], dp[n-1][k][d])
                    # print("a, n, k, d, a_rem_rev: ", a, n, k, d, a_rem_rev)
                    # print_dp(dp)


print(dp[N-1][K-1][0])