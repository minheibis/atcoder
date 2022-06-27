import numpy as np

large_num = 10 ** 9 + 1
n, m = map(int, input().split())

r_map = np.full((n + 1, n + 1), large_num)
print("r_map:", r_map)
ans_set = set()

for i in range(m):
    ans_can = i + 1
    start, end, len_se = map(int, input().split())
    print("start, end, len_se", start, end, len_se)
    if end < start:
        start, end = end, start

    if start == 1:
        if r_map[start, end] > len_se:
            r_map[start, end] = len_se
            ans_set.add(ans_can)
            print("direct")
            print("r_map:", r_map)
    else:
        for j in range(n + 1):
            if r_map[1, end] > r_map[1, start] + len_se:
                r_map[1, end] = r_map[1, start] + len_se
                ans_set.add(ans_can)
                print("indirect")
                print("r_map:", r_map)

print("r_map:", r_map)
print(*ans_set)