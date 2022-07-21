def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def bridge(g, n):
    result = set()
    label = [None] * n
    cost = [0] * n
    gen = 0

    def dfs(u, p):
        nonlocal gen
        res = 0
        for v in g[u]:
            if v == p:
                # is parent node, has already visited
                continue
            if label[v] is not None:
                # has visited but can go back
                if label[v] < label[u]:
                    cost[v] += 1
                    res += 1
            else:
                # has not visited
                label[v] = gen
                gen += 1
                r = dfs(v, u)
                if r == 0:
                    result.add((u,v) if u < v else (v, u))
                res += r
        res -= cost[u]
        return res

    for v in range(n):
        if not label[v]:
            label[v] = gen
            gen += 1
            r = dfs(v, -1)
    return result


n, m = nextInts()

# convert to adjacency list
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = nextInts()
    g[u-1].append(v-1) # do not forget to decrement. since 0 start
    g[v-1].append(u-1)

print(len(bridge(g, n)))