def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

from collections import defaultdict

N = nextInt()
s_list = list()
count_dict = defaultdict(int)
f_set = set(["H" , "D" , "C" , "S"])
s_set = set(["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"])

ans = "Yes"
for _ in range(N):
    s = str(input())
    if s[0] not in f_set:
        ans = "No"
    if s[1] not in s_set:
        ans = "No"
    count_dict[s] += 1

for s, i in count_dict.items():
    if i > 1:
        ans = "No"

print(ans)