# 基本的な解法
# 同じ横or縦位置でない場合には、4*4*1通りのテスト、出た結果が同じ縦or横位置の場合には、例外的にそこだけ2通りのテスト

t = int(input())
for _ in range(t):
    b, k, sx, sy, gx, gy = map(int, input().split())
    defsx, def_close_sx = divmod(sx, b)
    defsy, def_close_sy = divmod(sy, b)
    defgx, def_close_gx = divmod(gx, b)
    defgy, def_close_gy = divmod(gy, b)
    defsx *= b
    defsy *= b
    defgx *= b
    defgy *= b

    # for the start
    ans = (abs(sx - gx) + abs(sy - gy)) * k
    for i in range(4):
        if i == 0:
            tmpsx, close_sx = defsx, def_close_sx
            tmpsy, close_sy = sy, 0
        elif i == 1:
            tmpsx = defsx + b
            close_sx = b - def_close_sx
        elif i == 2:
            tmpsx, close_sx = sx, 0
            tmpsy, close_sy = defsy, def_close_sy
        elif i == 3:
            tmpsy = defsy + b
            close_sy = b - def_close_sy

        # for the goal
        for j in range(4):
            if j == 0:
                tmpgx, close_gx = defgx, def_close_gx
                tmpgy, close_gy = gy, 0
            elif j == 1:
                tmpgx = defgx + b
                close_gx = b - def_close_gx
            elif j == 2:
                tmpgx, close_gx = gx, 0
                tmpgy, close_gy = defgy, def_close_gy
            elif j == 3:
                tmpgy = defgy + b
                close_gy = b - def_close_gy

            # if for the same grid row or col
            # 1 patter or two pattern
            cell_tmpsx, close_tmpsx = divmod(tmpsx, b)
            cell_tmpgx, close_tmpgx = divmod(tmpgx, b)
            cell_tmpsy, close_tmpsy = divmod(tmpsy, b)
            cell_tmpgy, close_tmpgy = divmod(tmpgy, b)

            if cell_tmpsx == cell_tmpgx and cell_tmpsy != cell_tmpgy:
                close_x = close_tmpsx + close_tmpgx
                mid_len = min(
                    close_x,
                    b * 2 - close_x,
                )
                mid_len += abs(tmpsy - tmpgy)
            elif cell_tmpsy == cell_tmpgy and cell_tmpsx != cell_tmpgx:
                close_y = close_tmpsy + close_tmpgy
                mid_len = min(
                    close_y,
                    b * 2 - close_y,
                )
                mid_len += abs(tmpsx - tmpgx)     
            else:
                mid_len = abs(tmpsx - tmpgx) + abs(tmpsy - tmpgy)

            # print("tmpsx, tmpsy, tmpgx, tmpgy:", tmpsx, tmpsy, tmpgx, tmpgy)
            tmp_ans = (close_sx + close_sy + close_gx + close_gy) * k + mid_len * 1
            # print("close_sx, close_sy, close_gx, close_gy, mid_len, tmp_ans:", close_sx, close_sy, close_gx, close_gy, mid_len, tmp_ans)
            ans = min(ans, tmp_ans)
    print(int(ans))
