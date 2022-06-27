from collections import deque
from collections import Counter

N = int(input())
s_deq = deque(input())
let_couter = Counter(s_deq)
deq_let_counter = deque(sorted(let_couter.items(), key=lambda x:x[0]))

print("let_couter", let_couter)
print("deq_let_counter", deq_let_counter)

min_let = deq_let_counter.popleft()[0]
min_let_count = let_couter[min_let]

print(min_let, min_let_count)

ans_deq = deque()

start = 0
end = N
while len(s_deq) > 0:
    # 最初の文字は検索していく
    char_0 = s_deq.popleft()

    # ここで空になるかもしれない
    if len(s_deq) == 0:

        break

    # 最後の文字は消してOK
    char_1 = s_deq.pop()
    print("1 char_0, char_1", char_0, char_1)
    # どんなに右だとしてもその時点の最小値と交換したい。

    if char_0 == min_let:
        # char_0最小なら交換なし
        ans_deq.appendleft(char_0)
        ans_deq.append(char_1)

        let_couter[char_0] -= let_couter[char_0] - 1
        let_couter[char_1] -= let_couter[char_1] - 1

    elif char_1 == min_let:
        # char_1最小なら交換
        ans_deq.appendleft(char_1)
        ans_deq.append(char_0)

        let_couter[char_0] -= let_couter[char_0] - 1
        let_couter[char_1] -= let_couter[char_1] - 1

    else:
        ans_deq.append(char_1)
        let_couter[char_1] -= let_couter[char_1] - 1

        # char_1最小まで探し続ける。
        while (char_1 != min_let) and (len(s_deq) > 0):
            char_1 = s_deq.pop()
            print("2 char_0, char_1", char_0, char_1)
            # どんなに右だとしてもその時点の最小値と交換したい。
            # それまでは繰り返し
            if (char_1 == min_let):
                # 見つかったら交換
                ans_deq.appendleft(char_1)
                ans_deq.append(char_0)

                let_couter[char_0] -= let_couter[char_0] - 1
                let_couter[char_1] -= let_couter[char_1] - 1

            else:
                ans_deq.append(char_1)
                let_couter[char_1] -= let_couter[char_1] - 1

    if let_couter[min_let] == 0:
        min_let = deq_let_counter.pop_left()[0]

print("".join(ans_deq))