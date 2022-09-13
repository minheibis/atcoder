# https://atcoder.jp/contests/dp/submissions/34782087
# 文字列は重いので、メモリに載せない。長さだけで管理して、後ろから一番長いやつを取り出していく。
S = str(input())
T = str(input())

dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

length = dp[len(S)][len(T)]

slen = len(S) - 1
tlen = len(T) - 1

res = []

while length > 0:
    if S[slen] == T[tlen]:
        res.append(S[slen])
        slen -= 1
        tlen -= 1
        length -= 1
    else:
        if dp[slen + 1][tlen + 1] == dp[slen][tlen + 1]:
            slen -= 1
        else:
            tlen -= 1

print("".join(res[::-1]))
