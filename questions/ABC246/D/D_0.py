import math

N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    sum_a_b = math.ceil(N ** (1/3))
    # print(sum_a_b)

    max_func = sum_a_b ** 3
    # print(max_func)
    max_minus = max_func - N
    # print("max_minus", max_minus)

    not_max = False
    for a in range(int(sum_a_b / 2) + 1):
        # print(a)
        b = sum_a_b - a
        mul_a_b = 2 * sum_a_b * (a * b)
        # print(a,b,mul_a_b)
        if max_minus < mul_a_b:
            not_max = True
            break

    if not_max:
        a -= 1
        b += 1
        mul_a_b = 2 * sum_a_b * (a * b)

    print(max_func - mul_a_b)
