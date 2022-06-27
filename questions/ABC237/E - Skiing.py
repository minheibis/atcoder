H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

# 繋がっているところの整理

# 全探索の場合
while len(M_list) > 0:
    # スタート地点から始めて、可能性を並列させていく。