#https://atcoder.jp/contests/abc236/submissions/28789973

N = int(input())
A = list(map(int, input().split()))

def is_ok(X):
    use = no_use = 0
    for x in X:
        use, no_use = max(use, no_use) + x, use # 同時に行うことで、tmpを使わない
    return max(use, no_use)

def average():
    ok = 0
    ng = 10**9 + 1
    while (abs(ng - ok) > 1e-3):
        m = (ok + ng) / 2 # mという値で引くことで、その値を達成できるかどうかを探索する。
        if is_ok([a - m for a in A]) >= 0:
            ok = m
        else:
            ng = m
    return ok

def median():
    ok = 0
    ng = 10**9 + 1
    while abs(ok - ng) > 1:
        m = (ok + ng) // 2 # mという値で引くことで、その値を達成できるかどうかを探索する。
        if is_ok([-1 if a < m else 1 for a in A]) > 0:
            ok = m
        else:
            ng = m
    return ok

print(average())
print(median())