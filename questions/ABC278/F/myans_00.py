from collections import defaultdict
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


n = nextInt()
v = defaultdict(list)
for i in range(n):
    s = str(input())
    v[s[0]].append(s[-1])

print(v)

def choose_rec(visit, start):
    if len(tmp_v) == 0:
        return
    else:
        for start_dict in tmp_v:
            for start in start_dict.


ans_flag = choose_rec(v, 1)
if ans_flag:
    print("First")
else:
    print("Second")