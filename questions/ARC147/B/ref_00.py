# https://atcoder.jp/contests/arc147/submissions/34636074

import sys
N = int(sys.stdin.readline().rstrip())
P = [ int(x) for x in sys.stdin.readline().rstrip().split() ]

ans = []

for i in range(N-2):
    for j in range(N-3, i-1, -1):
        if (j+1)%2 == P[j]%2 and (j+3)%2 != P[j+2]%2:
            P[j], P[j+2]  = P[j+2], P[j]
            ans.append(['B', j+1])

for i in range(N-1):
    if (i+1)%2 != P[i]%2 and (i+2)%2 != P[i+1]%2:
            P[i], P[i+1]  = P[i+1], P[i]
            ans.append(['A', i+1])

for i in range(N-2):
    for j in range(N-3, i-1, -1):
        if P[j] > P[j+2]:
            P[j], P[j+2]  = P[j+2], P[j]
            ans.append(['B', j+1])
print(len(ans))
for el in ans:
    print("{} {}".format(el[0], el[1]))