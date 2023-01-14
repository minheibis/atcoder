from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



# 入力を受け取る
N, M = map(int, input().split())
uf = UnionFind(N)
uf_p = UnionFind(N * 2)

G = [set() for _ in range(N)]  # グラフを表現する隣接リスト

is_close = False
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    u_a = a
    v_a = a + N
    u_b = b
    v_b = b + N
    # 頂点 a から頂点 b への辺を張る
    G[a].add(b)
    # 無向グラフのため、頂点 b から頂点 a への辺も張る
    G[b].add(a)

    uf.union(a, b)

    uf_p.union(u_a, v_b)
    uf_p.union(u_b, v_a)

ans = 0
for i in range(N):
    print(i)
    connected = uf.size(i)
    not_connected = N - connected
    memb = uf_p.members(i)
    other_par = 0
    for j in memb:
        if j >= N:
            other_par += 1
    connected_ok = connected - len(G[i]) - other_par
    print(not_connected, connected_ok)
    ans += not_connected
    if connected_ok > 0:
        ans += connected_ok
print(ans)