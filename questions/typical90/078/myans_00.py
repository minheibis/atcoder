n, m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0
for i, p in enumerate(g):
    count = 0
    for j in p:
        if j < (i + 1):
            count += 1
    if count == 1:
        ans += 1

print(ans)