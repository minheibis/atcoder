# https://atcoder.jp/contests/abc259/submissions/33167664
n = int(input())

a = []

from collections import deque, Counter, defaultdict
maxnum = defaultdict(int)
ignore = defaultdict(int)

for i in range(n):
    m = int(input())
    ai = []
    for j in range(m):
        p,e = map(int, input().split())
        if maxnum[p] == e:
            ignore[p] = e
        maxnum[p] = max(maxnum[p],e)
        ai.append((p,e))
    a.append(ai)

s = set()

for ai in a:
    tmp = []
    for p,e in ai:
        if maxnum[p] == e and ignore[p] != e:
            tmp.append(p)
    tmp.sort()
    s.add(tuple(tmp))

print(len(s))


        