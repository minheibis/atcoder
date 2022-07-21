def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
from collections import defaultdict

n = nextInt()
# input
LCM_dict = defaultdict(int)
ignore_dict = defaultdict(int)
a = [] # input list

for i in range(n):
    m = nextInt()
    ai = []
    for j in range(m):
        p, e = nextInts()
        if LCM_dict[p] == e:
            # if it has max already then does not have to count
            ignore_dict[p] = e
        LCM_dict[p] = max(LCM_dict[p], e)
        ai.append((p, e))
    a.append(ai)

s = set()
ans = 0
zero_Flag = False # to find the max LCM
for ai in a:
    tmp = []
    flag = False # to find the LCM which has changed from maxLCM
    for p, e in ai:
        if LCM_dict[p] == e and ignore_dict[p] != e:
            flag = True
    if flag == True:
        ans += 1
    elif flag == False and zero_Flag == False:
        ans += 1
        zero_Flag = True

print(ans)