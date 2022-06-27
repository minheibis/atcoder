# 入力を受け取る
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 配列の右端をok, 左端をngと設定する。それぞれ端から１ずれているのは、両端が未判定のため。
ok = N
ng = -1

# while文で繰り返し真ん中の値を調べていく。while文を抜け出す条件は、okとngが隣り合う（差が1になる）まで
while abs(ok - ng) > 1:

# 真ん中の値をmidに代入
  mid = (ok + ng) // 2

# 真ん中の値がK以上ならokにmidを、そうでなければ、ngにmidを代入
  if A[mid] >= K:
    ok = mid
  else:
    ng = mid

# whileの処理により、okに入っている値は、K以上を満たす最小の値。
# okが最初の値と変わっていない時、条件をみたすものがない。
if ok != N:
  print(ok)
else:
  print(-1)
