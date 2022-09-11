from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set([input() for _ in range(M)])

def f(cur, rem):
    if len(rem) == 1:
        cur = cur + rem
        cur = ''.join(cur)
        if 3 <= len(cur) <= 16 and cur not in T:
            exit(print(cur))
        else:
            return
    num = 16 - len(cur) - 1 - (len(rem) - 1) - (len(rem) - 2)
    while 0 < num:
        f(cur + [rem[0]] + ['_'] * num, rem[1:])
        num -= 1
    return
    
for x in permutations(S):
    f([], list(x))

print(-1)