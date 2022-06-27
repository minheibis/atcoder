# 速度不足です

from copy import deepcopy
from collections import deque

N = int(input()) 
#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
A = [list(reversed(list(map(int, input().split())))) for l in range(2 * N - 1)]

# print(N)
# print(A)

# n組の組み合わせを並列で作っていって、それぞれ評価を行う。
deq_score_and_map = deque([(0, A)])
for i in range(N):
    #print("deq_score_and_map: ", deq_score_and_map)
    deq_score_and_map_new = deque()
    # それぞれ並列で処理
    for score_and_map in deq_score_and_map:
        # その時点の最上位の行の要素の数だけ通りが考えられる。
        old_map = score_and_map[1]
        old_map_first = old_map[0]
        len_old_map_first = len(old_map_first)
        for j, score in enumerate(old_map_first):
            # print("j, score: ", j, score)
            new_score = score_and_map[0] ^ score
            # 使われた相手を除く
            inv_num = len_old_map_first - j + 1
            new_map = [
                    [
                        old_map[row_num][col_num]
                         for col_num in range(len(old_map[row_num])) if (col_num != j)
                    ]
                     for row_num in range(len_old_map_first) if ((row_num != 0) and (row_num != inv_num - 1))
                ]
            deq_score_and_map_new.append((new_score, new_map))
    deq_score_and_map = deq_score_and_map_new

# print("last: ", sorted(deq_score_and_map))
print(sorted(deq_score_and_map)[-1][0])
