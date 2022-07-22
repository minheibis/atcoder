n, q = map(int, input().split())
a = list(map(int, input().split()))

r = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x = (x-r-1) % n
    y = (y-r-1) % n
    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        r += 1
    else:
        print(a[x])

