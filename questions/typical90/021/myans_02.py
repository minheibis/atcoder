# ref: https://atcoder.jp/contests/typical90/submissions/27898154

import sys
sys.setrecursionlimit(10**7)

# 入力
N, M = map(int, input().split())

edge = [[] for _ in range(N)]
redge = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    redge[B].append(A)

# dfsの１回目

has_visited = [False for _ in range(N)]
record_order = []

def dfs(now):
    has_visited[now] = True
    for next in edge[now]:
        if has_visited[next]:
            continue
        dfs(next)
    record_order.append(now)


for now in range(N):
    if has_visited[now]:
        continue # 訪問済みであれば、そこはスキップする
    dfs(now) # dfsを行って、全てのノードに対して帰りがけ順を記録する

record_order.reverse() # 帰りがけ順の数字が大きい方から、次のdfsは行いたい

# dfsの2回目

has_visited_2 = [False for _ in range(N)]
components = [] # グループを格納する

def rdfs(now):
    has_visited_2[now] = True
    components[-1].append(now)  # 今扱っているグループに、xを追加する。
    for next in redge[now]:
        if has_visited_2[next]:
            continue
        rdfs(next)

for now in range(N):
    if has_visited_2[now]:
        continue
    components.append([])
    rdfs(now)

# 答えを計算する部分

ans = 0
for component in components:
    n = len(component)
    ans += n * (n-1) // 2
print(ans)
