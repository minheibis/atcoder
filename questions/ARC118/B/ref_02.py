# https://atcoder.jp/contests/arc118/submissions/22249102
# https://www.headboost.jp/numpy-argpartition/
# https://zenn.dev/reputeless/books/standard-cpp-for-competitive-programming/viewer/library-algorithm
# https://stackoverflow.com/questions/29145520/how-is-nth-element-implemented

import numpy as np

K, N, M = map(int, input().split())
A = np.array(input().split(), np.int64)

B = M * A // N
C = N * B - M * A
n = M - B.sum()

ids = np.argpartition(C, n)[:n]

B[ids] += 1
print(*B)
