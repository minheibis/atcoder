# 速度不足です

from copy import deepcopy

N = int(input()) 
#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
A = [list(reversed(list(map(int, input().split())))) for l in range(2 * N - 1)]

# print(N)
# print(A)

# n組の組み合わせを並列で作っていって、それぞれ評価を行う。
list_score_and_map = [(0, A)]
for i in range(N):
    #print("list_score_and_map: ", list_score_and_map)
    list_score_and_map_new = []
    # それぞれ並列で処理
    for score_and_map in list_score_and_map:
        # その時点の最上位の行の要素の数だけ通りが考えられる。
        old_map_first = score_and_map[1][0]
        len_old_map_first = len(old_map_first)
        for j, score in enumerate(old_map_first):
            # print("j, score: ", j, score)
            new_score = score_and_map[0] ^ score
            # コピー兼使用した行の削除
            new_map = score_and_map[1][1:]
            # print("new_map_start", new_map)
            # 使われた相手を除く
            inv_num = len_old_map_first - j + 1
            # print("inv_num", inv_num)
            # 行の削除
            if inv_num - 2 < len(new_map):
                new_map.pop(inv_num - 2)
                # print("new_map.pop(inv_num - 2)", new_map)
            # 列の削除
            for list_row in new_map:
                if j < len(list_row):
                    list_row.pop(j)
                    # print("list_row.pop(j)", new_map)
            # print("new_score", new_score)
            # print("new_map: ", new_map)
            list_score_and_map_new.append((new_score, new_map))
    list_score_and_map = list_score_and_map_new

# print("last: ", sorted(list_score_and_map))
print(sorted(list_score_and_map)[-1][0])
