a, N = map(int, input().split())

num_list = [1]
count = 0
while True:
    if min(num_list) > N:
        print(-1)
        break
    else:
        #操作2
        flag = False
        num_list_add = []
        for i in num_list:
            if i >= 10 and i % 10 != 0:
                flag = True
                i_str = str(i)
                len_i = len(i_str)
                i_2_list = [i]
                for j in range(len_i - 1):
                    i_str_next = i_str[len_i - 1] + i_str[0:len_i - 1]
                    i_str = i_str_next
                    i_2_list.append(int(i_str))
                num_list_add += i_2_list
        if flag == True:
            count += 1
            num_list += list(set(num_list_add))
            print("2, count, num_list", count, num_list)
            if N in num_list:
                print(count)
                break
    # 操作1    
    num_list = list(set([i*a for i in num_list]))
    count += 1
    print("1, count, num_list", count, num_list)
    if N in num_list:
        print(count)
        break