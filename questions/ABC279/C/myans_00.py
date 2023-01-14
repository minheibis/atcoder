from collections import Counter

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

H, W = nextInts()
s = []
t = []
for _ in range(H):
    s.append(list(str(input())))
for _ in range(H):
    t.append(list(str(input())))

s_c = Counter()
t_c = Counter()

for i in range(W):
    s_row = ""
    t_row = ""
    for j in range(H):
        s_row += s[j][i]
        t_row += t[j][i]
    s_c[s_row] += 1
    t_c[t_row] += 1

ans = "Yes"
for s_key, s_value in s_c.items():
    if t_c[s_key] != s_value:
        ans = "No"

print(ans)
