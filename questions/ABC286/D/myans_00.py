from collections import defaultdict
from copy import deepcopy
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, X = nextInts()
A_set = set()
wallet = dict()
for i in range(N):
    A, B = nextInts()
    A_set.add(A)
    wallet[A] = B

dp = [[] for _ in range(X + 1)]
for x in range(1, X+1):
    for a in A_set:
        if x == a:
            init_dict = defaultdict(int)
            init_dict[a] = 1
            dp[a].append(init_dict)
        if x - a > 0:
            for tmp_dict in dp[x-a]:
                if tmp_dict[a] < wallet[a]:
                    tmp_dict_new = deepcopy(tmp_dict)
                    tmp_dict_new[a] += 1
                    dp[x].append(tmp_dict_new)
# print(dp)
if len(dp[X]) > 0:
    print("Yes")
else:
    print("No")