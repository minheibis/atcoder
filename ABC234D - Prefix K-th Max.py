def pos_search(N, A, x):
    if x > A[0]:
        return 0
    l = 0
    r = N - 1
    if r == 1:
        return 1
    while r - l > 1:
        m = (l + r) // 2
        #print("l, r, m, A[m]", l, r, m, A[m])
        if x < A[m]:
            l = m
        if x > A[m]:
            r = m
    return m + 1

N, K = map(int, input().split())
p_list = list(map(int, input().split()))
#print(p_list)

p_list[0:K] = sorted(p_list[0:K], reverse=True)
#print(p_list)
print(p_list[K - 1])

for i in range(K, N):
    #print("p_list[i-1]", p_list[i-1])
    #print("p_list[i]", p_list[i])
    #print("i", i)
    if p_list[i-1] < p_list[i]:
        pos = pos_search(i, p_list[0:i], p_list[i])
        print("pos", pos)
        tmp = p_list[i]
        p_list[pos+1:i+1] = p_list[pos:i]
        p_list[pos] = tmp
    print(p_list)
    print(p_list[K - 1])

    
