from collections import defaultdict
from collections import deque

def change_k_let(k_let, mod_num):
    let_list = [0, 1, 2]
    index_now = let_list.index(k_let)
    if mod_num == 0:
        new_index = (index_now - 1) % 3
    else:
        new_index = (index_now + 1) % 3
    return let_list[new_index]

char_list = ["A", "B", "C"]

s_0 = str(input())
q = int(input())
query_list = []
for i in range(q):
    query_list.append(list(map(int, input().split())))



for i, query in enumerate(query_list):
    # print("query: ", query)
    t = query[0]
    k = query[1]
    k_let = 0
    k_let_last = k_let

    for j in range(t):
        k, mod_num = divmod(k + 1, 2)
        # print("j, k, mod_num:", j, k, mod_num)
        # 順次もとまるのでは？
        k_let = change_k_let(k_let, mod_num)
        # print("k_let", k_let)

        # k_letが1になってしまったら、もう先頭確定なので。割り算を続ける必要はない
        if k == 1:
            # print("remain j:", j)
            # print("remain t - j:", t - j)
            break

    # 最後にずらす
    if t == 0:
        print(char_list[k - 1])
    else:
        let_index_moved = (k_let_last - k_let) + (t - j - 1)
        let_start = s_0[k - 1]
        let_start_index = char_list.index(let_start)
        let_last_index = (let_start_index + let_index_moved) % 3
        # print("let_last_index: ", let_last_index)
        print(char_list[let_last_index])
# 同時に割り算していけるのでは？