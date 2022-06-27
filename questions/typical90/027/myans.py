# python のsetは1で判断

n = int(input())
name_set = set()

for i in range(n):
    name = str(input())
    if name not in name_set:
        print(i + 1)
        name_set.add(name)  