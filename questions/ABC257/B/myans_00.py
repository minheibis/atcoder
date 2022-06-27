N, K, Q = map(int, input().split())

# 0マス目は使わない
n_list = [0] * (N + 1)
a_list = list(map(int, input().split()))
l_list = list(map(int, input().split()))

for a in a_list :
    n_list[a] = 1
print("n_list: ", n_list)

for l in l_list:
    print(l)
    if l == N:
        continue
    elif n_list[l + 1] != 1:
        n_list[l + 1] = 1
        n_list[l] = 0
print("n_list: ", n_list)