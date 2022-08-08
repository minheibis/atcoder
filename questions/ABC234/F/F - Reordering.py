import math

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r) 

S_list = list(str(input()))
alpha_list = list("abcdefghijklmnopqrstuvwxyz")
S_count_list = [
    S_list.count(i) for i in alpha_list
]

sum_count_list = []
tmp = 0
for i in range(26):
    tmp += S_count_list[i]
    sum_count_list.append(tmp)

len_S = len(S_list)
MOD = 998244353

dp = [[0] * (len_S + 1) for _ in range(26)]
for j in range(S_count_list[0]+1):
    dp[0][j] = 1
#print("dp", dp)

for i in range(1, 26):
    for j in range(sum_count_list[i] + 1):
        for k in range(min(S_count_list[i], j) + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-k] * permutations_count(j, k)) % MOD

print(sum(dp[-1][1:]) % MOD)