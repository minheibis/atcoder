A, B, C, X = map(int, input().split())

if X <= A:
    print(float(1))
elif X <= B:
    p = C / (B - A)
    print(float(p))
else:
    print(float(0))
