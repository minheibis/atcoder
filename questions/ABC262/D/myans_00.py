from collections import defaultdict
from itertools import product
from math import factorial

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
a_list = nextIntList()

ans = 0
for i in range(1, n+1):
    d = defaultdict(int)
    for a in a_list:
        d[a % i] += 1
    # print("i: ", i)
    # print(d)
    comb_all = product(d.keys(), repeat=i)
    tmp_ans = 0
    for comb in comb_all:
        # print(comb)
        if sum(comb) % i == 0:
            # print("can devide")
            tmp_tmp_ans = 1
            key_count = defaultdict(int)
            for key in comb:
                tmp_count = d[key] - key_count[key]
                tmp_tmp_ans *= tmp_count
                # print("key, tmp_count, tmp_tmp_ans", key, tmp_count, tmp_tmp_ans)
                key_count[key] += 1
            tmp_ans += tmp_tmp_ans
    # print("tmp_ans_before:", tmp_ans)
    tmp_ans //= factorial(i)
    # print("tmp_ans:", tmp_ans)
    ans += tmp_ans

print(ans)