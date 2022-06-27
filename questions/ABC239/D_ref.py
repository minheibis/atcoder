import time

primes_list = []          # このリストに素数を保存していく
upper_lim   = 10000       # テキトーな数を設定
start_time  = time.time() # 開始時刻を記録

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

print(primes_list)
print(len(primes_list), "prime numbers foud.")

elapsed_time = time.time() - start_time # 経過時間 = 現在時刻 - 開始時刻
print ("run time: {0}".format(elapsed_time) + " seconds")