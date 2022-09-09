# https://atcoder.jp/contests/typical90/submissions/34622835

N = int(input())
links = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

def dfs(sx):
    que = [(sx, -1)]
    D = [0] * N
    while que:
        x, par = que.pop()
        for nx in links[x]:
            if nx == par:
                continue
            D[nx] = D[x] + 1
            que.append((nx, x))
    resd = -1
    for i, d in enumerate(D):
        if d > resd:
            resd = d
            resp = i
    return resp, resd          

s, _ = dfs(0)
_, ans = dfs(s)
print(ans + 1)