s = str(input())
len_s = len(s)

rep = 6 // len_s
ans = ""
for i in range(rep):
    ans += s

print(ans)