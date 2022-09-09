from collections import defaultdict
from itertools import product
from queue import Queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# 実装は、https://note.nkmk.me/python-union-find/より
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

class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members

def solve():
    H, W = nextInts()
    Q = nextInt()

    labels = list(product(range(H), range(W)))
    red_set = set()
    # # print("labels: ", labels)

    uf = UnionFindLabel(labels)
    # # print("uf: ", uf)

    for num in range(Q):
        q = nextIntList()
        # print("num:", num)
        # print("q: ", q)


        if q[0] == 1:
            r, c = q[1]-1, q[2]-1
            red_set.add((r, c))

            # print("red_set:", red_set)

            red_around = Queue()
            for (i, j) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                # do not have to check if not out of map, since it is set
                if (r+i, c+j) in red_set:
                    red_around.put((r+i, c+j))

            # print("red_around: ", red_around.queue)
            # join the red cells
            while not red_around.empty():
                next_cel = red_around.get()
                uf.union((r, c), next_cel)

        elif q[0] == 2:
            if (uf.same((q[1]-1, q[2]-1), (q[3]-1, q[4]-1))) and ((q[1]-1, q[2]-1) in red_set):
                print("Yes")
            else:
                print("No")

        # print("uf:", uf)

solve()