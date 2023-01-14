from collections import Counter
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

H, W, N, h, w = nextInts()
A = []
all_c = Counter()

for i in range(H):
    A.append(nextIntList())
for i in range(H):
    for j in range(W):
        all_c[A[i][j]] += 1
# print("all_c: ", all_c)

for i in range(0, H-h+1):
    ans_list = []
    for j in range(0, W-w+1):
        ans = 0
        tmp_c = Counter()
        for tmp_i in range(i, i+h):
            for tmp_j in range(j, j+w):
                tmp_c[A[tmp_i][tmp_j]] += 1
        # print("tmp_c :", tmp_c)
        for num in range(1, N+1):
            if all_c[num] - tmp_c[num] > 0:
                ans += 1
        ans_list.append(ans)
    print(*ans_list)
