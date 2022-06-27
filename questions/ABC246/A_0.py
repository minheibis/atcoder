from collections import Counter

x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_count = Counter(x_list)
y_count = Counter(y_list)

ans_list = []

for x, count in x_count.items():
    if count == 1:
        ans_list.append(x)

for y, count in y_count.items():
    if count == 1:
        ans_list.append(y)


print(*ans_list)