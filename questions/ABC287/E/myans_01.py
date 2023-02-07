from collections import Counter, defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MAX_N = 5 * 10**5
N = nextInt()
s_list = list()
len_list = list()
max_s = 0

s_dict_list = [
    defaultdict(int) for _ in range(MAX_N + 1)
]

for i in range(N):
    s = str(input())
    s_list.append((i, s))
    len_s = len(s)
    len_list.append(len_s)
    max_s = max(max_s, len_s)
    for j in range(len_s):
        s_dict_list[j][s[:j]] += 1

ans_list = [0 for _ in range(N)]
tmp_len = 0
while len(s_list) > 0:
    print(s_list)
    for s in s_list:
        if s_dict_list[j][s[1][:tmp_len]] < 2:
            ans_list[s[0]] = tmp_len
            s_list.remove(s)
    tmp_len += 1

for ans in ans_list:
    print(ans)

