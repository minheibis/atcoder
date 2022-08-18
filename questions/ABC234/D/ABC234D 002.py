N, K = map(int, input().split())
p_list = list(map(int, input().split()))

head_list = sorted(p_list[0:K], reverse=True)
print(head_list[K - 1])

for i in range(K, N):
    #print("p_list[i-1]", p_list[i-1])
    #print("p_list[i]", p_list[i])
    #print("i", i)
    if head_list[K - 1] < p_list[i]:
        head_list.append(p_list[i])
        head_list.sort(reverse=True)
        #print(head_list)
    print(head_list[K - 1])
