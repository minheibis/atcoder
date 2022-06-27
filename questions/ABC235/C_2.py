import collections

N, Q = map(int, input().split())
a_list = list(map(int, input().split()))
a_list_set = set(a_list)
a_list_counter = collections.Counter(a_list)

x_list = []
for i in range(Q):
    x_one = list(map(int, input().split()))
    x_list.append(x_one)

a_count_dict = {}
for a_num in a_list_set:
    a_count_dict[a_num] = []

for i, a in enumerate(a_list):
    if a in a_list_set:
        a_count_dict[a].append(i + 1)

for x_one in x_list:
    x, k = x_one[0], x_one[1]
    if x not in a_list_set:
        print(-1)
    elif a_list_counter[x] < k:
        print(-1)
    else:
        print(a_count_dict[x][k - 1])
