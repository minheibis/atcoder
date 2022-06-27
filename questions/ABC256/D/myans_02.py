import numpy as np

max_num = 2 * (10 ** 5) + 2
# print(max_num)
ans_list = np.zeros(max_num)

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    ans_list[l:r] = 1
    # print(ans_list)

# print(np.where(ans_list==1))

comp_list = np.insert(ans_list, 0, 0)[0:-1]
flag_list = ans_list - comp_list

start_list = np.where(flag_list==-1)[0]
end_list = np.where(flag_list==1)[0]

for start, end in zip(start_list, end_list):
    print(end, start)