from scipy.special import comb

from collections import Counter
n = int(input())

a_l = list(map(str, input().split()))

c = Counter(a_l)
# print(c)

all_count = (comb(n, 3, exact=True))
# print(all_count)

for num, value in c.items():
    if value >= 2:
        rm_value = n - value
        less_count = (comb(value, 2, exact=True)) * rm_value
        all_count -= less_count
    if value >= 3:
        less_count = (comb(value, 3, exact=True))
        all_count -= less_count
print(all_count)