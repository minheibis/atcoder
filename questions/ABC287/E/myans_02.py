from collections import Counter, defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MAX_N = 5 * 10**5
N = nextInt()
s_list = list()
len_list = list()
max_s = 0

for i in range(N):
    s = str(input())
    s_list.append((i, s))
    len_s = len(s)
    len_list.append(len_s)
    max_s = max(max_s, len_s)

ans_list = [0 for _ in range(N)]
while len(s_list):
    for s in s_list.

for ans in ans_list:
    print(ans)