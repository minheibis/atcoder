import numpy as np

max_num = 2 * (10 ** 5) + 1
# print(max_num)
# max_num = 60
ans_list = np.zeros(max_num)

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    ans_list[l:r] = 1
    # print(ans_list)

ans = []
open_flag = False
for j, i in enumerate(ans_list):
    if open_flag == False:
        if i == 1:
            start = j
            open_flag = True
    else:
        if i == 0:
            end = j
            ans.append([start, end])
            open_flag = False

for tmp in ans:
    print(*tmp)
