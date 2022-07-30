def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, X = map(int, input().split())
q = 2**30 - 1
print("X, q:", X, q)
for _ in range(n):
    t, a = map(int, input().split())
    print("t, a:", t, a)
    if t == 1:
        q &= a
    elif t == 2:
        q |= a
    elif t == 3:
        q ^= a
    print("X, q:", X, q)
    X &= q
    print(X)