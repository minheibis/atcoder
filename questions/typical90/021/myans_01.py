# ref: https://atcoder.jp/contests/typical90/submissions/27898154

import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())

edge = [[] for _ in range(N)]
redge = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    redge[B].append(A)

come = [False] * N # 通ったかの判定

backorder = []

def dfs(x):
    come[x] = True
    for to in edge[x]:
        if come[to]:continue
        dfs(to)
    backorder.append(x)

components = []
    
def rdfs(x):
    come[x] = True
    components[-1].append(x) # 今扱っているグループに、xを追加する。
    for to in redge[x]: # reverse(G)に対して行う
        if come[to]:continue
        rdfs(to)

# ここから実際の計算部分

for v in range(N):
    if come[v]:continue
    dfs(v)

backorder.reverse()  # 帰りがけ順の数字が大きい方から、次のdfsは行いたい

come = [False] * N # いったんリセット
for v in backorder:
    if come[v]:continue # いったことない頂点 v が出てきたら、新しいグループを追加して、rdfs(v)を行う。いったことのある頂点はスルーする。
    components.append([]) # 新しいグループを追加する。
    rdfs(v)


# 答えを計算する部分

ans = 0
for component in components:
    n = len(component)
    ans += n * (n-1) // 2
print(ans)
