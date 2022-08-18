N = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

a_score = sum(a_list[0::2])
b_score = sum(a_list[1::2])

print(a_score - b_score)