

from collections import deque
from collections import Counter
import copy

N = int(input())
s_list = list(input())
let_couter = Counter(s_list)
deq_let_counter = deque(sorted(let_couter.items(), key=lambda x:x[0]))

# print("let_couter", let_couter)
# print("deq_let_counter", deq_let_counter)

min_let = deq_let_counter.popleft()[0]
min_let_count = let_couter[min_let]

# print(min_let, min_let_count)
ans_list = copy.deepcopy(s_list)

start = 0
end = len(s_list) - 1

while start < end:
    # 最初の文字は検索していく
    char_0 = s_list[start]
    # ここで空になるかもしれない
    if start == end:
        # 交換なし
        break

    # 最後の文字は消してOK
    char_1 = s_list[end]
    # print("1 char_0, char_1", char_0, char_1)

    # どんなに右だとしてもその時点の最小値と交換したい。
    if char_0 == min_let:
        # char_0最小なら交換なし
        start += 1
        end -= 1
        let_couter[char_0] = let_couter[char_0] - 1
        let_couter[char_1] = let_couter[char_1] - 1

    elif char_1 == min_let:
        # char_1最小なら交換
        ans_list[start], ans_list[end] = ans_list[end], ans_list[start]

        start += 1
        end -= 1
        let_couter[char_0] = let_couter[char_0] - 1
        let_couter[char_1] = let_couter[char_1] - 1

    else:
        end -= 1
        let_couter[char_1] = let_couter[char_1] - 1

        # char_1最小まで探し続ける。
        while (char_1 != min_let) and (start < end):
            char_1 = s_list[end]
            # print("2 char_0, char_1", char_0, char_1)
            # どんなに右だとしてもその時点の最小値と交換したい。
            # それまでは繰り返し
            if (char_1 == min_let):
                # 見つかったら交換
                # print(ans_list)
                ans_list[start], ans_list[end] = ans_list[end], ans_list[start]
                # print(start, end)
                # print(ans_list)
                start += 1
                end -= 1

                let_couter[char_0] = let_couter[char_0] - 1
                let_couter[char_1] = let_couter[char_1] - 1
                # print("min_let", min_let)
                # print("let_couter[min_let]", let_couter[min_let])

            else:
                # 見つからなければ不交換
                end -= 1
                let_couter[char_1] = let_couter[char_1] - 1

    # print("min_let", min_let)
    # print("let_couter[min_let]", let_couter[min_let])
    # print("let_couter", let_couter)
    if let_couter[min_let] == 0:
        # 最小値の更新
        if (len(deq_let_counter) > 0):
            min_let = deq_let_counter.popleft()[0]
        # print("min_let", min_let)
    
    # print("ans_list_tmp", ans_list)

print("".join(ans_list))