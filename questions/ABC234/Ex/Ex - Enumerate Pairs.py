n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]

ans = set()
dic = {}

base = 10 ** 10

for i, (x, y) in enumerate(XY):
    # x += base
    # y += base
    ix = x // k
    iy = y // k
    if (ix, iy) not in dic:
        dic[(ix, iy)] = []
    
    dic[(ix, iy)].append(i)

for (ix, iy), lis in dic.items():
    for i in range(len(lis)):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (ix+dx, iy+dy) not in dic:
                    continue
                for j in dic[(ix+dx, iy+dy)]:
                    x, y = XY[lis[i]]
                    nx, ny = XY[j]

                    if (x - nx)**2 + (y - ny)**2 > k**2:
                        continue
                    a = lis[i]
                    b = j
                    if a == b:
                        continue
                    if a > b:
                        a, b = b, a
                    ans.add((a, b))

print(len(ans))
ans = sorted(list(ans))
for x, y in ans:
    print(x+1, y+1)