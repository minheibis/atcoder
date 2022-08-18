def down_stair(start_num, diff_num, len_X):
#    print(start_num, diff_num, len_X)
#    print(type(start_num), type(diff_num), type(len_X))    
    # same numもこちらに含む
    down_str = str(start_num)
    next_num = start_num
#    print(down_str, next_num)
    for i in range(len_X - 1):
        next_num -= diff_num
        down_str += str(next_num)
#        print(down_str)
    return int(down_str)

def up_stair(start_num, diff_num, len_X):
    up_str = str(start_num)
    next_num = start_num
    for i in range(len_X - 1):
        next_num += diff_num
        up_str += str(next_num)
    return int(up_str)

def calc(X):
    str_X = str(X)
    len_X = len(str_X)
    start_num = int(str_X[0])
    a = 10e18
    b = 10e18
    
    # 1. 1桁の場合
    if len_X == 1:
        return X

    # 2-1. 1桁目同じでdown-same stair（下から）
#    print("int(start_num) // (len_X - 1) + 1", int(start_num) // (len_X - 1) + 1)
    for diff_num in reversed(range(0, int(start_num) // (len_X - 1) + 1)):
#        print("down diff_num", diff_num)
        ans = down_stair(start_num, diff_num, len_X)
#        print(ans)
        if ans >= X:
            return ans

    # 2-2. 1桁目同じでup stair（下から）
#    print("(9 - int(start_num)) // (len_X - 1) + 1", (9 - int(start_num)) // (len_X - 1) + 1)
    for diff_num in range(1, (9 - int(start_num)) // (len_X - 1) + 1):
#        print("up diff_num", diff_num)
        ans = up_stair(start_num, diff_num, len_X)
#        print(ans)
        if ans >= X:
            return ans

    # 3. 1桁目をインクリメントして、down-same stair（下から）
    start_num += 1
    for diff_num in reversed(range(0, int(start_num) // (len_X - 1) + 1)):
#        print("plus diff_num", diff_num)
        ans = down_stair(start_num, diff_num, len_X)
#        print(ans)
        if ans >= X:
            return ans

X = int(input())
print(calc(X))