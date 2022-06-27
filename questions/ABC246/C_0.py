from collections import deque
import bisect 

N, K, X = map(int, input().split())
a_deq = deque((map(int, input().split())))
small_list = list()

# # print(a_deq)
while bool(a_deq) == True:
    # print("tmp a_deq: ", a_deq)
    # まずは、Xより大きいものについて使う
    a = a_deq.popleft()
    # print("tmp a:", a)
    if a < X:
        # Xより小さいものはdeqに格納
        # 並べ替えもしたい。
        bisect.insort(small_list, a)
    elif K <= 0:
        # もうKがない時も入れていく。
        bisect.insort(small_list, a)
    else:
        # modを使って計算を高速化する。
        tmp_num_K, tmp_a = divmod(a, X)
        tmp_rem_K = K - tmp_num_K
        if tmp_rem_K >= 0:
            # 完全に割っても大丈夫なら、そのまま続行
            K = tmp_rem_K
            a = tmp_a
            # print("a up", a)
        else:
            # 負になってしまったら、現在のKを全て使うところまで
            a -= (X * K)
            K = 0
            # print("a down", a)
        # print("next a:", a)
        a_deq.append(a)

# print(a_deq)
# print("small_list", small_list)

max_len = len(small_list)
i = max_len - 1
while K > 0 and i >= 0:
    small_list[i] = 0
    i -= 1
    K -= 1
    # Xより大きいものがなくなったとき、今度は小さいものについて、大きい順に使っていく。
    # deqがなくなる or K

# print(small_list)
print(sum(small_list))