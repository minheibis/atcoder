import copy

a, N = map(int, input().split())
N_keta = 10 ** len(str(N))
#print("N_keta", N_keta)

num_set = set([1])
num_set_all = copy.copy(num_set)

count = 0
while True:
    count += 1
    num_set_new = set()
    for i in list(num_set):
        if i >= N_keta:
            #print(i)
            continue
        # 操作1
        i_new = i * a
        num_set_new.add(i_new)

        # 操作2
        if i >= 10 and i % 10 != 0:
            flag = True
            i_str = str(i)
            len_i = len(i_str)
            i_next = int(i_str[len_i - 1] + i_str[0:len_i - 1])
            if i_next not in num_set_all:
                num_set_new.add(i_next)
    num_set_all = num_set_all | num_set_new
    #print("num_set_all", num_set_all)
    num_set = num_set_new
    #print("num_set", num_set)

    if N in num_set:
        print(count)
        break
    
    #print("min", min(num_set))
    if min(num_set) > N:
        print(-1)
        break

#    if count > 20:
#        break
