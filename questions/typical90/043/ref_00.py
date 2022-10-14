# https://ebinafactory.hatenablog.com/entry/2021/10/17/183736

from collections import deque
H,W = [int(x) for x in input().split()]
rs, cs = [int(x)-1 for x in input().split()]
rt, ct = [int(x)-1 for x in input().split()]
S = [input() for _ in range(H)]

# A[r][c]は、(r,c)にたどり着くまでの曲がった回数
INF = float("inf")
A = [[INF] * W for _ in range(H)]

# 探索済(開始地点は-1にしておく)
A[rs][cs] = -1

# BFS用にこれから探索する場所をキューに入れる(
openpos = deque()
openpos.append((rs,cs))

# キューの頭から展開していく
while (len(openpos) != 0):
    p = openpos.popleft()
    r, c = p[0], p[1]
    cnt = A[r][c] + 1
    # 上下左右
    D = [(-1,0), (+1,0), (0,-1), (0,+1)]
    for d in D:
        rr = r
        cc = c
        while True:
            rr += d[0]
            cc += d[1]
            # 道であり、まだ未探索ならそこから探索できるようにキューに足す。
            if (0<=rr<H) and (0<=cc<W): #
                if S[rr][cc] == "." and A[rr][cc]>A[r][c]:
                    A[rr][cc] = cnt
                    openpos.append((rr,cc))
                else:
                    break
            else:
                break

# 開始地点は0に戻しておく
A[rs][cs] = 0
print(A[rt][ct])