import numpy as np


H, W = map(int, input().split())
A = [list(map(int, input().split())) for l in range(H)]

A = np.array(A)

row_sum = np.sum(A, axis=1).reshape(-1, 1)
col_sum = np.sum(A, axis=0)

ans = row_sum + col_sum - A

for row in ans:
    print(*row)