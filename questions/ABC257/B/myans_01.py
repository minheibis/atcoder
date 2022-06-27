N, K, Q = map(int, input().split())

a_list = list(map(int, input().split()))
l_list = list(map(int, input().split()))

for l in l_list:
    l -= 1
    # print(l)
    if a_list[l] == N:
        continue
    elif l + 1 == len(a_list):
        a_list[l] += 1
    elif a_list[l + 1] != a_list[l] + 1:
        a_list[l] += 1
# print("a_list: ", a_list)
print(*a_list)