q = int(input())
l = list()
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        # 計算量:O(n)
        l = [x] + l
    elif t == 2:
        # 計算量:O(1)
        l.append(x)
    elif t == 3:
        # 計算量:O(1)
        print(l[x-1])