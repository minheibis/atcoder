# 参考: https://atcoder.jp/contests/abc268/submissions/34779689
from itertools import permutations

N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]
T = set([str(input()) for _ in range(M)])

def f(cur, rem):
    if len(rem) == 1:
        # last rem
        cur += rem
        cur = "".join(cur)
        if 3 <= len(cur) <= 16 and cur not in T:
            print(cur)
            exit()
        else:
            return False
    # ありうるアンダーバーの個数は、残りの個数も意識して残す必要がある。
    num = 16 - len(cur) - 1 - (2 * (len(rem) - 1)) + 1
    while 0 < num:
        # ありうるアンダーバーの個数分のnumをそれぞれ試していく。
        f(cur + [rem[0]] + ["_"] * num, rem[1:])
        num -= 1
    return

for x in permutations(S):
    f([], list(x))
print("-1")