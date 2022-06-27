MOD = 998244353
N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1

edge = []
for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edge.append((U, V))

for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edge.append((U, V))

for i in range(K):
    for U, V in edge:
        for x in range(2):
            dp[x][i + 1][V] += dp[x ^ (V == X)][i][U]
            if dp[x][i + 1][V] >= MOD:
                dp[x][i + 1][V] -= MOD
            dp[x][i + 1][U] += dp[x ^ (U == X)][i][V]
            if dp[x][i + 1][U] >= MOD:
                dp[x][i + 1][U] -= MOD
print(dp[0][K][T])