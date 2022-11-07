from itertools import permutations

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
P = nextIntList()
P_tup = tuple(P)

per_list = list(permutations(sorted(P)))
per_len = len(per_list)

l, r = 0, per_len - 1
while l < r - 1:
    # print(l, r)
    m = (l + r) // 2
    if per_list[m] < P_tup:
        l = m
    else:
        r = m
print(*per_list[l-1])