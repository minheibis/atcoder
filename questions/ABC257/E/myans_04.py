from calendar import c


n = int(input())
c_list = list(map(int, input().split()))
min_c = min(c_list)
keta = n // min_c
rem = n - (keta - 1) * min_c
# print(keta, rem)
loop_num = [i for i, x in enumerate(c_list) if x == min_c][-1] + 1
first_num = [i for i, x in enumerate(c_list) if x <= rem][-1] + 1
# print(first_num, loop_num)

if keta == 0:
    print("0")
else:
    print(str(first_num) + str(loop_num) * (keta - 1))

# n = int(input())
c = c_list

min_c = min(c)
d = n // min_c
rem = n % min_c
loop_digit = max(i+1 for i, ci in enumerate(c) if ci == min_c)

head_digit = ""
for i in range(9, 0, -1):
    di = c[i-1] - min_c
    if di == 0 or i < loop_digit:
        continue
    k = rem // di
    rem %= di
    head_digit += str(i) * k


print((head_digit + str(loop_digit) * (d))[:d])