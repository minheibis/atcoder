def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
from collections import defaultdict

n = nextInt()
# input
LCM_list = [defaultdict(int) for _ in range(n)]
maxcount_dict = defaultdict(int)

for i in range(n):
    m = nextInt()
    for _ in range(m):
        p, e = nextInts()
        for j, LCM_dict in enumerate(LCM_list):
            if i == j:
                continue
            else:
                if e == LCM_dict[p]:
                    maxcount_dict[p] += 1
                elif e > LCM_dict[p]:
                    LCM_dict[p] = e
                    maxcount_dict[p] = 1
                    
print("LCM_list:", LCM_list)
print("maxcount_dict:", maxcount_dict)

LCM_set = set()
for LCM_dict in LCM_list:
    LCM_set.add(tuple(LCM_dict.items()))

# print(LCM_set)
print(len(LCM_set))