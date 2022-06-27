# https://atcoder.jp/contests/abc238/editorial/3350

# N = int(input())

def question_c(N):
    N_str = str(N)
    digit_len = len(N_str)
    MOD = 998244353

    def sum_of_cont_num(a, b):
        MOD = 998244353
        ab_sum = (a + b) % MOD
        ab_sub = (b - a + 1) % MOD
        return (((ab_sum * ab_sub) % MOD) / 2)

    def sum_for_digit(digit, count):
        if digit == 1:
            return sum_of_cont_num(1, count)
        else:
            # print("1, count + 1", 1, count + 1)
            return sum_of_cont_num(1, count + 1)

    ans = 0
    # print("digit_len", digit_len)
    for digit_inv, num in enumerate(N_str):
        # 桁数
        digit = digit_len - digit_inv
        # print("digit, num", digit, num)
        if digit == digit_len:
            # 一番上の桁の場合
            if digit == 1:
                rem_val = int(num)
            else:
                base_num = 10**(digit - 1)
                rem_val = N - base_num
            # print("digit, rem_val", digit, rem_val)
            add_num = sum_for_digit(digit, rem_val) % MOD
            # print("add_num_first", add_num)
            ans = (ans + add_num) % MOD
        else:
            if digit == 1:
                rem_val = 9
            else:
                rem_val = (10**(digit) - 1) - 10**(digit - 1)
            # print("digit, rem_val", digit, rem_val)
            add_num = sum_for_digit(digit, rem_val) % MOD
            # print("add_num", add_num)
            ans = (ans + add_num) % MOD
        # print(ans)

    # print(int(ans % MOD))
    return int(ans % MOD)

former_val = 0
for i in range(1000000000, 1100000000):
    this_val = question_c(i)
    print("i, c: ", i, this_val, this_val - former_val)
    former_val = this_val
    