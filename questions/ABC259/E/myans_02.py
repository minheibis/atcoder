def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
from collections import defaultdict

n = nextInt()
# input
LCM_dict_all = defaultdict(int)
pair_list = [defaultdict(int) for _ in range(n)]
for pair_dict in pair_list:
    m = nextInt()
    for _ in range(m):
        p, e = nextInts()
        pair_dict[p] = e
        LCM_dict_all[p] = max(e, LCM_dict_all[p])
        # 内部で更新してしまいたい？

print("pair_list:", pair_list)
print("LCM_dict_all:", LCM_dict_all)

ans = 0
for key, val in LCM_dict_all.items():
    # print("key, val:", key, val)
    count = 0
    # if it has unique max, then have to count up
    for pair_dict in pair_list:
        if pair_dict[key] == val:
            # print("pair_dict: ", pair_dict)
            count += 1
    if count == 1:
        ans += 1
 
print(min(ans + 1, n))