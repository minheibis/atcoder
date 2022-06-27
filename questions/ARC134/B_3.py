# 参考：https://atcoder.jp/contests/arc134/submissions/28869708

N = int(input())
S = list(input())
# Sを変換
X = [ord(S[i]) - ord("a") for i in range(N)]
C = [[-1] * (N + 1) for i in range(26)] # 先頭が1文字多い（インデックスの都合）

# そのiの時点で一番右側にあるその文字のインデックスを保存している。
for i in range(N):
    for j in range(26):
        C[j][i + 1] = C[j][i] #C[X[i]][i+1] = iで指定した文字を次にもコピー
    # 次の文字の指定している。
    C[X[i]][i+1] = i
    # print("C in loop:", i, C)

## print("X", X)
## print("C", C)

R = N # 右端をセット
for L in range(N):
    # 左から順にインクリメント
    # print("L", "X[L]", L, X[L])
    for k in range(X[L]): #相手となる文字の検索, aから順番にX[L]の文字になるまで探せばいい。
        # print("k", k)
        # print("L, C[k][R]", L, C[k][R])
        if L < C[k][R]: # その文字の右端の場所がC[k][R]に記録してある。その場所より左にある時。
            R = C[k][R]  # 記録してある場所を右端として指定。
            S[L], S[R] = S[R], S[L]  # 左右を交換
            break

print("".join(S))