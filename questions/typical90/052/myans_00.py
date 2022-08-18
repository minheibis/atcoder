DICE_LEN = 6
MOD = 10 ** 9 + 7

n = int(input())
dices = []
for i in range(n):
    dices.append(list(map(int, input().split())))

dp = [[0 for _ in range(DICE_LEN)] for _ in range(n)]
for j in range(DICE_LEN):
    dp[0][j] = dices[0][j]

for i in range(1, n):
    for j in range(DICE_LEN):
            for k in range(DICE_LEN):
                dp[i][j] += ((dp[i-1][k] * dices[i][j]) % MOD)
                dp[i][j] %= MOD

print(sum(dp[n-1]) % MOD)