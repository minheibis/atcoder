from collections import defaultdict
import sys

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
        #print(self.n)
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

it = map(int, sys.stdin.buffer.read().split())
N, M, Q = next(it), next(it), next(it)
es = []
for u, v, w in zip(it, it, it):
    # 重みを最初に入れることで、後でソートに使っている。
    es.append((w, u, v, len(es)))

print(es)
es.sort()
print(es)
uf = UnionFind(N + 1)
answer = [None] * Q

for e in es:
    print(uf)
    w, u, v, q = e
    if q >= M:
        if uf.same(u, v):
            answer[q - M] = "No"
        else:
            answer[q - M] = "Yes"
    else:
        uf.union(u, v)

print(*answer, sep="\n")