h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a11 in range(1, 29):
    for a12 in range(1, 29):
        for a21 in range(1, 29):
            for a22 in range(1, 29):
                a13 = h1 - a11 - a12
                a23 = h2 - a21 - a22
                a31 = w1 - a11 - a21
                a32 = w2 - a12 - a22
                a33_h = h3 - a31 - a32
                a33_w = w3 - a13 - a23
                if a33_h == a33_w:
                    if a13 > 0 and a23 > 0 and a31 > 0 and a32 > 0 and a33_h > 0:
                        # print([[a11, a12 ,a13], [a21, a22, a23], [a31, a32, a33_h, a33_w]])
                        ans += 1

print(ans)