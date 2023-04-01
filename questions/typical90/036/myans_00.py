from collections import defaultdict, deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, Q = nextInts()
list_p = []
for _ in range(N):
    x, y = nextInts()
    list_p.append((x, y))

list_q = []
for _ in range(Q):
    list_q.append(nextInt() - 1)

# 1. x+y, x-y に座標変換を行う。
# 2. 変換した後のx, y　座標の最大値、最小値を記録しておく（写真2の4つの値）。
list_new_p = []
for i, (old_x, old_y) in enumerate(list_p):
    new_x = old_x + old_y
    new_y = old_x - old_y
    list_new_p.append((new_x, new_y))
    if i == 0:
        max_x, min_x = new_x, new_x
        max_y, min_y = new_y, new_y
    else:
        max_x = max(max_x, new_x)
        min_x = min(min_x, new_x)
        max_y = max(max_y, new_y)
        min_y = min(min_y, new_y)

# 3. それぞれのクエリについて、写真2の4つの値との差の絶対値を計算していく。その4つの絶対値の最大値が求める答え

for q in list_q:
    x, y = list_new_p[q]
    ans = max(
        abs(max_x - x),
        abs(min_x - x),
        abs(max_y - y),
        abs(min_y - y),
    )
    print(ans)