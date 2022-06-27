from collections import defaultdict

s_0 = str(input())
q = int(input())
query_list = []
for i in range(q):
    query_list.append(list(map(int, input().split())))

print(s_0)
print(q)
print(query_list)

s = s_0
for i in range(10):
    s = s.translate(str.maketrans({'A': 'BC', 'B': 'CA', 'C': 'AB'}))
    print(s)