from collections import deque

N = int(input())
S_list = list(input())

ans_l = list([0])
ans_r = list()

index_now = 0
for i, c in enumerate(S_list):
    if c == "L":
        ans.insert(index_now,i + 1)
        index_now = index_now
    else:
        ans.insert(index_now + 1, i + 1)
        index_now = index_now + 1

ans = ans_l + ans_r
#print(ans)
print(" ".join(map(str, ans)))