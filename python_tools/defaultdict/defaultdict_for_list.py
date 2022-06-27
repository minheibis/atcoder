from collections import defaultdict

s = [
    ("yellow", 1),
    ("blue", 2),
    ("yellow", 3),
    ("bule", 4),
    ("red", 1)
]

d = defaultdict(list)
print("d", d)
for k, v in s:
    # listを設定したために、appendが使えるようになっている。
    d[k].append(v)
    print("d", d)

print(list(d.items()))