import numpy as np

n = int(input())
m = np.array([list(input()) for i in range(n)])

def check_row(row):
    len_row = len(row)
    count_row = [0 for _ in range(len_row + 1)]
    # まずはプラス、マイナスを記録
    max_len = 0
    count_row[0] = 0
    for i, one_char in enumerate(row):
        if one_char == "#":
            max_len += 1
        else:
            # 白の場合
            max_len -= 1
        count_row[i + 1] = max_len
    
    # 探す
    for i in range(len_row + 1 - 6):
        start = count_row[i]
        end = count_row[i + 6]
        if end - start >= 2:
            return True
    return False

def check_all(n, m):
    for i in range(n):
        # print("col", i, check_row(m[i]))
        if check_row(m[i]) == True:
            print("Yes")
            return
    m_T = m.T
    for i in range(n):
        # print("row", i, check_row(m_T[i]))
        if check_row(m_T[i]) == True:
            print("Yes")
            return
    # 斜め1
    # 可能な範囲分実行する。
    diag_count_half = n - 5
    for i in range(0 - diag_count_half, 0 + diag_count_half + 1):
        row_tmp = np.diag(m, k = i)
        # print("diag", i, check_row(row_tmp))
        if check_row(row_tmp)== True:
            print("Yes")
            return

    # 斜め2
    m_lr = np.fliplr(m)
    diag_count_half = n - 5
    for i in range(0 - diag_count_half, 0 + diag_count_half + 1):
        row_tmp = np.diag(m_lr, k = i)
        # print("diag", i, check_row(row_tmp))
        if check_row(row_tmp)== True:
            print("Yes")
            return

    print("No")
    return

check_all(n, m)