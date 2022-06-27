# 【Python】漸化式で実装する動的計画法（DP）
# https://qiita.com/keisuke-ota/items/504d66092671a67c1040

#N = int(input())
#h = list(map(int,input().split()))
N = 5
h = [1, 3, 4, 5, 6]

# DP配列
dp = [0] * N

# 初期条件
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# 漸化式に従ったDPを実装する
for i in range(2, N):
    # i を現在いる足場とする
    # i 番目の足場に行く方法として、i-ばんめからのジャンプとi-2ばんめからのジャンプを比較する
    dp[i] = min(
        dp[i - 2] + abs(h[i] - h[i-2]),
        dp[i - 1] + abs(h[i] - h[i-1])
    )

print(dp[-1])