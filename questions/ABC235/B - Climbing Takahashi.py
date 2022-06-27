N = int(input())
h_list = list(map(int, input().split()))

#print(N)
#print(h_list)

for i in range(len(h_list)):
    if i == len(h_list) - 1:
        break
    if h_list[i] >= h_list[i + 1]:
        break
print(h_list[i])