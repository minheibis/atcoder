# 方針
# T + A個の中に連続t_len個以上の素数ではない区間があればTの勝ち
# 素数を探すには、たかだか T + A のsqrtの素数まで探せばいい。
import math
import numpy as np

A, B, C, D = map(int, input().split())

def f(A, B, C, D):
    min_num = A + C
    max_num = B + D
    t_len = D - C + 1

    base_list = [i for i in range(min_num, max_num + 1)]
    # print("base_list: ", base_list)

    # 素数探し
    # 素数リスト
    primes_list = []          # このリストに素数を保存していく
    if max_num == 2:
        upper_lim = 2
    elif max_num == 3:
        upper_lim = 3
    else:
        upper_lim = int(math.sqrt(max_num))     # テキトーな数を設定

    for integer in range(2, upper_lim + 1, 1): # 2-10000の整数に対して、
        if len(primes_list) < 1 :              # primes_listが空だったら、
            primes_list.append(integer)        # primes_listにinteger(=2)を追加する
        else:                                  # その他の場合（本題）、
            is_divisible = False               # integerが割り切れない、つまり素数であることを仮定する
            for prime in primes_list:          # 今までに保存された全ての素数"prime"について、
                if integer % prime == 0:       # integerがprimeで割り切れるならば
                    is_divisible = True        # 割り切れます（つまり素数じゃない）
                    break                      # そしたらもうこのforはやる意味がないです。
            # integerが合成数ならどっかのprimeでis_divisible = Trueになる
            if not is_divisible:               # すべてのprimeについてこの判定をしたのち、それでもなおis_divisible = Falseならばもうそれは素数
                primes_list.append(integer)    # integerを素数として認め、primes_listに追加する
    # print("primes_list: ", primes_list)

    # 判定
    for prime_num in primes_list:
        base_list = [i for i in base_list if i % prime_num != 0 or i == prime_num]
    # print("base_list_after: ", base_list)

    # interval_list
    base_list = [min_num - 1] + base_list
    base_list.append(max_num + 1)
    base_array = np.array(base_list)
    interval_array = base_array[1:] - base_array[:-1]
    # print("interval_array: ", interval_array)

    # interval_lenの計算
    if len(interval_array) == 0:
        print("Aoki")
    else:
        interval_len = interval_array.max() - 1
        if interval_len >= t_len:
            print("Takahashi")
        else:
            print("Aoki")

f(A, B, C, D)