max_num = 2 * (10 ** 5)
# print(max_num)
# max_num = 60
ans_list = [0 for _ in range(max_num)]

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    ans_list[l:r] = [1 for _ in list(range(l, r))]
    # print(ans_list)

ans = 0
open_flag = False
for i in ans_list:
    if open_flag == False:
        if i == 1:
            ans += 1
            open_flag = True
    else:
        if i == 0:
            open_flag = False

print(ans)
