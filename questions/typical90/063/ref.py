# https://logicalbear.net/%E3%80%90%E7%AB%B6%E3%83%97%E3%83%AD%E5%85%B8%E5%9E%8B90%E5%95%8F%E3%80%91%E3%80%8C063-monochromatic-subgrid%EF%BC%88%E2%98%854%EF%BC%89%E3%80%8D%E8%A7%A3%E6%B3%95/

from collections import Counter, defaultdict
from itertools import product

def solve():
    H, W = map(int, input().split())
    arr_map = [
        list(map(int, input().split())) for _ in range(H)
    ]

    # 行をビット全探索
    patterns = product((False, True), repeat=H)
    ans = 0
    for p in patterns:
        select_h = [] # 選択する行のリスト
        for i in range(H):
            if p[i]:
                select_h.append(i)

        # 選択する行が0行の場合
        if len(select_h) == 0:
            continue
        # 選択する行が1行の場合
        elif len(select_h) == 1:
            c = Counter(arr_map[0])
            ans = max(ans, c.most_common()[0][1])

        # 選択する行が2行以上の場合
        else:
            cnt_w = defaultdict(int)
            for j in range(W):
                # 列を1つずつ見ていき、選択した全ての行で同じ文字だった場合に、cnt_wの値を増やす
                val = arr_map[select_h[0]][j]
                if all(arr_map[i][j] == val for i in select_h):
                    cnt_w[val] += 1
            if not cnt_w:
                max_w = 0
            else:
                max_w = max(cnt_w.values())
            ans = max(ans, len(select_h)*max_w)
    print(ans)

solve()