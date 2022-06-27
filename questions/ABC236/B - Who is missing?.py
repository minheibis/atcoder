from collections import Counter

N = int(input())
a_list = list(map(int, input().split()))

#print("N:", N)
#print("a_list", a_list)

a_c = Counter(a_list)

for k, v in a_c.items():
    if v == 3:
        print(k)
        break