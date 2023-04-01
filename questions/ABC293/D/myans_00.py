def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# union plus count

from collections import defaultdict

class UnionFindPathCount():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.path_counts = [0] * n
        self.member_counts = [1] * n

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
            self.path_counts[x] += 1 # if already same, just add 1
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x


        self.parents[x] += self.parents[y]
        self.path_counts[x] += self.path_counts[y]
        self.member_counts[x] += self.member_counts[y]

        self.parents[y] = x
        self.path_counts[x] += 1 # the path is add again here

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        ## print(self.n)
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

    def get_path_counts(self, x):
        return self.path_counts[self.find(x)]

    def get_member_counts(self, x):
        return self.member_counts[self.find(x)]

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = nextInts()
uf = UnionFindPathCount(N)
for _ in range(M):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    uf.union(a, c)

root_list = uf.roots()
# print(root_list)
ans_sum = len(root_list)
ans_yes = 0

for root_node in root_list:
    # print("root_node: ", root_node)
    # print("uf.members(): ", uf.members(root_node))
    # print("uf.get_member_counts(root_node): ", uf.get_member_counts(root_node))
    # print("uf.get_path_counts(root_node): ", uf.get_path_counts(root_node))

    if uf.get_path_counts(root_node) == uf.get_member_counts(root_node):
        ans_yes += 1

ans_no = ans_sum - ans_yes
print(ans_yes, ans_no)