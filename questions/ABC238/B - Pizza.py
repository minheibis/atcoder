N = int(input())
A = list(map(int, input().split()))

p_list = [0] * 361

p_list[0] = 1
p_list[360] = 1
a_sum = 0
for a in A:
    a_sum = a_sum + a
    a_sum = a_sum % 360
    # print(a_sum)
    p_list[a_sum] = 1

# print(p_list)

max_len = 0
start_i = 0
for i, val in enumerate(p_list):
    if val == 1:
        # print("i", i)
        tmp_len = i - start_i
        start_i = i
        if tmp_len > max_len:
            max_len = tmp_len

print(max_len)
