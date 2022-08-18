n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a[x-1], a[y-1] = a[y-1], a[x-1]
    elif t == 2:
        a.insert(0, a.pop())
    else:
        print(a[x-1])

