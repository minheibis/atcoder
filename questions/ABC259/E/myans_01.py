def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
from collections import defaultdict

n = nextInt()
# input
LCM_dict_all = defaultdict(int)
LCM_list = [defaultdict(int) for _ in range(n)]
for i in range(n):
    m = nextInt()
    for _ in range(m):
        p, e = nextInts()
        for j, LCM_dict in enumerate(LCM_list):
            if i == j:
                continue
            else:
                LCM_dict[p] = max(e, LCM_dict[p])

            LCM_dict_all[p] = max(e, LCM_dict_all[p])

            # 内部で更新してしまいたい？

print("LCM_list:", LCM_list)
print("LCM_dict_all:", LCM_dict_all)

LCM_set = set()
for LCM_dict in LCM_list:
    # if it has unique max, then have to count up
    LCM_tup = list()
    for key, val in LCM_dict_all.items():
        LCM_tup.append(val - LCM_dict[key])
    LCM_set.add(tuple(LCM_tup))

print(LCM_set)
print(len(LCM_set))