S_list = list(map(str, input().split()))
T_list = list(map(str, input().split()))
S_num_list = [i for i in range(0, 3)]

c_dict = dict()
for i in S_num_list:
    c_dict[S_list[i]] = i
T_num_list = []
for c in T_list:
    T_num_list.append(c_dict[c])

#print(S_num_list)
#print(T_num_list)

if T_num_list == [0, 1, 2] or T_num_list == [1, 2, 0] or T_num_list == [2, 0, 1]:
    print("Yes")
else:
    print("No")