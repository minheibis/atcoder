def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, m = nextInts()
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
# print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

 
ans = 0
for i in range(n):
    for j in graph[i]:
        for k in graph[j]:
            if k in graph[i]:
                # print(i, j, k)
                ans += 1

print(ans // 6)