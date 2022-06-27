import sys
from collections import Counter

n, m = map(int, input().split())
pre_list = list(map(int, input().split()))
eat_list = list(map(int, input().split()))

c = Counter(pre_list)

for eat_now in eat_list:
    c[eat_now] -= 1
    if c[eat_now] < 0:
        print("No")
        sys.exit()
print("Yes")