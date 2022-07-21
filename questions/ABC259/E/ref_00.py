# https://atcoder.jp/contests/abc259/submissions/33137463

from collections import defaultdict
from heapq import *

N = int(input())
A = []

lib = defaultdict(lambda: defaultdict(int))
cnt = defaultdict(int)
for _ in range(N):
    M = int(input())
    t = []
    for _ in range(M):
        p,e = map(int, input().split())
        t.append((p,e))
        lib[p][e]+=1
        cnt[p] = max(cnt[p],e)
    A.append(t)

print("A:", A)
print("cnt:", cnt)
print("lib:", lib)

ans = 0
g = 0
for a in A:
    fit = 0
    for p,e in a:
        if e==cnt[p] and lib[p][e]==1:
            fit = 1
    if not fit and g==0:
        fit = 1
        g = 1
    ans+=fit

print(ans)

