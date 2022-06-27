n = int(input())
set_a = set()
max_num = 0
max_i = 0

for i in range(n):
    s, num = map(str, input().split())
    if s not in set_a:
        set_a.add(s)
        num = int(num)
        if num > max_num:
            max_num = num
            max_i = (i + 1)

print(max_i)