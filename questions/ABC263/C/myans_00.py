def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())  

import itertools

n, m = nextInts()
m_list = [i for i in range(1,m+1)]
ans_list = itertools.combinations(m_list, n)

for ans in ans_list:
    print(*ans)