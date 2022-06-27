import collections

N, Q = map(int, input().split())
a_list = list(map(int, input().split()))
a_list_set = set(a_list)
a_list_counter = collections.Counter(a_list)

x_list = []
for i in range(Q):
    x_one = list(map(int, input().split()))
    x_list.append(x_one)

#print(N, Q)
#print(a_list)
#print(x_list)
#print(a_list_counter)

for x_one in x_list:
    x, k = x_one[0], x_one[1]
    if x not in a_list_set:
        print(-1)
    elif a_list_counter[x] < k:
        print(-1)
    else:
        count = 0
        #print("x, k", x, k)
        for i, a in enumerate(a_list):
            #print("a", a)
            if a == x:
                count = count + 1
            if count == k:
                print(i + 1)
                break