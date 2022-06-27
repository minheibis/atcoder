# 基本的には8進数を9進数に描き直す問題
# ここに現れる数字「 8 」を「 5 」に書き直す
# この部分はあまり本質とは関係ない。

import numpy as np

def mod_8_to_10(n_list):
    n_10 = 0
    n_list.reverse()
    for i, n_char in enumerate(n_list):
        n_10 += int(n_char) * (8 ** i)
        # print("n_10 in mod8:", n_10)
    return n_10

n, k = map(int, input().split())
n_list = list(str(n))

for i in range(k):
    # print("n_list:", n_list)
    n_10 = mod_8_to_10(n_list)
    # print("n_10:", n_10)

    n = np.base_repr(n_10, 9)
    # print("n:", n)

    str_n = str(n)
    str_n = str_n.replace("8", "5")
    n_list = list(str_n)

print(int("".join(n_list)))