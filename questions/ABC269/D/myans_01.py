def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

from collections import defaultdict
from queue import Queue


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

around_xy = [
    (-1, -1),
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
    (1, 1)
]

SIZE = 2000
SIZE_ONE = 2001
WIDTH = SIZE * 2 + 1

def solve():
    def rc_to_index(r, c):
        index = (r + SIZE) * WIDTH + c + SIZE
        return index

    N = nextInt()
    uf = UnionFind(WIDTH * WIDTH)
    black_set = set()

    # add black set
    # join the red cells
    for _ in range(N):
        r, c = nextInts()
        rc_index = rc_to_index(r, c)
        black_set.add(rc_index)

        # do union for the cells black around
        red_around = Queue()
        for (i, j) in around_xy:
            # have to check if not out of map
            if ((r+i >= -SIZE and r+i <= SIZE and c+j >= -SIZE and c+j <= SIZE)
                and rc_to_index(r+i, c+j) in black_set):
                red_around.put(rc_to_index(r+i, c+j))

        while not red_around.empty():
            next_cel = red_around.get()
            # print("rc_index, next_cel", rc_index, next_cel)
            uf.union(rc_index, next_cel)

    black_roots = [i for i, x in enumerate(uf.parents) if x < 0 and i in black_set]
    print(len(black_roots))

solve()