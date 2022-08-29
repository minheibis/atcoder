def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

import numpy as np

# パリティっぽいな
H, W = nextInts()
A, B = [], []
for _ in range(H):
    A.append(nextIntList())
for _ in range(H):
    B.append(nextIntList())
A = np.array(A)
B = np.array(B)
C = B - A
# print("A: ", A)
# print("B: ", B)
# print("B-A: ", B-A)

ans = 0
for i in range(H-1):
    for j in range(W-1):
        diff = C[i][j] - 0
        C[i][j] = C[i][j] - diff
        C[i+1][j] = C[i+1][j] - diff
        C[i][j+1] = C[i][j+1] - diff
        C[i+1][j+1] = C[i+1][j+1] - diff
        ans += abs(diff)

if np.all(C == 0):
    print("Yes")
    print(ans)
else:
    print("No")