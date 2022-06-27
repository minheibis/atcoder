H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

#print("H, W", H, W)
#print("A", A)

B = [list(x) for x in zip(*A)]

for row in B:
    print(*row)
