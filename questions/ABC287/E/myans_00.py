from collections import Counter, defaultdict
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
s_list = list()
len_list = list()
max_s = 0
for _ in range(N):
    s = str(input())
    s_list.append(s)
    len_s = len(s)
    len_list.append(len_s)
    max_s = max(max_s, len_s)
    
letter_dict_list = list()
for i in range(max_s):
    letter_dict = defaultdict(int)
    for s, len_s in zip(s_list, len_list):
        if i < len_s:
            letter_dict[s[i]] += 1
    letter_dict_list.append(letter_dict)

for s in s_list:
    ans = 0
    for i, c in enumerate(s):
        if letter_dict_list[i][c] < 2:
            break
        ans += 1
    print(ans)