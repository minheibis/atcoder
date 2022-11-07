from itertools import permutations

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
P = nextIntList()
P_tup = tuple(P)

per_list = list(permutations(sorted(P)))
per_len = len(per_list)

for i, P_tmp in :
    # print("per_list[i+1]: ", per_list[i+1])
    # print("P_tup ", P_tup)
    if per_list[i+1] == P_tup:
        print(*per_list[i])