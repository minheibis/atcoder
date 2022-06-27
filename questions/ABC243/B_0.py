N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

same = 0
for a, b in zip(a_list, b_list):
    if a == b:
        same+=1

print(same)
print(len(list(set(a_list) & set(b_list))) - same)
