from itertools import combinations

MOD = 998244353

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def print_dp(dp):
    for l in range(0, n+1):
        print(dp[l])


n = nextInt()
a_list = [0] + nextIntList()

dp = [[[0 for k in range(n)] for j in range(n + 1)] for i in range(n + 1)]
# 余りは0<=k<=n-1, 選ぶ数は1<=j<=i, 全体の範囲は1<=i<=n
# 全体の範囲は1<=i<=n, 選ぶ数は1<=j<=i, 余りは0<=k<=n-1

dp[0][0][0] = 1
print_dp(dp)

for i in range(1, n+1):
    print("\n")
    print("a_list[i]:", a_list[i])
    for j in range(0, i+1):
        for k in range(0, i):
            print("i, j, k:", i, j, k)
            dp[i][j][k] += dp[i-1][j][k] # まず前回分まで
            if j + 1 <= i:
                new_k = (k + a_list[i]) % (j+1) # if adding i
                print("i-1, j, k:", i-1, j, k)
                print("i, j+1, new_k:", i, j+1, new_k)
                dp[i][j+1][new_k] += dp[i-1][j][k] # 当てはまるものを加算していく.
            else:
                print("j+1 > i")
            print_dp(dp)

ans = 0
for j in range(1, n+1):
    ans += dp[n][j][0]
print(ans)