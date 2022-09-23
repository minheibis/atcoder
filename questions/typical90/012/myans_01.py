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


def solve():
    def rc_to_index(r, c):
        index = (r - 1) * W + c - 1
        return index

    H, W = nextInts()
    Q = nextInt()

    uf = UnionFind(H * W)
    red_set = set()

    for num in range(Q):
        q = nextIntList()

        if q[0] == 1:
            # 連結クエリ
            r, c = q[1], q[2]
            rc_index = rc_to_index(r, c)
            red_set.add(rc_index)

            red_around = Queue()
            for (i, j) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                # have to check if not out of map
                if ((r+i >= 1 and r+i <= H and c+j >= 1 and c+j <= W)
                    and rc_to_index(r+i, c+j) in red_set):
                    red_around.put(rc_to_index(r+i, c+j))

            # join the red cells
            while not red_around.empty():
                next_cel = red_around.get()
                uf.union(rc_index, next_cel)

        elif q[0] == 2:
            # 判定クエリ
            if ((uf.same(rc_to_index(q[1], q[2]), rc_to_index(q[3], q[4])))
                and (rc_to_index(q[1], q[2]) in red_set)):
                print("Yes")
            else:
                print("No")

solve()