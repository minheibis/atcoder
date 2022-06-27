def main():
    N, K = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    tmp_list = [True, True]
    for i in range(N-1):
        # print(tmp_list)
        a0 = list_a[i]
        a1 = list_a[i + 1]
        b0 = list_b[i]
        b1 = list_b[i + 1]
        new_tmp_list = [False, False]
        for j, check_open in enumerate(tmp_list):
            if check_open == True:
                # 開いている方を検証
                if j == 0:
                    num_now = a0
                else:
                    num_now = b0
                # print(num_now, a1, b1, K)
                if abs(num_now - a1) <= K:
                    # 更新
                    # print("if abs(num_now - a1) <= K")
                    new_tmp_list[0] = True
                if abs(num_now - b1) <= K:
                    # 更新
                    new_tmp_list[1] = True
                # print(new_tmp_list)
        if (new_tmp_list[0] == False) and (new_tmp_list[1] == False):
            print("No")
            return
        tmp_list = new_tmp_list

    print("Yes")
    return

main()