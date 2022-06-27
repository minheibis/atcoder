from collections import deque

N = int(input())
S_list = deque(list(input()))
S_list.reverse()
S_list.append("L")

# print(S_list)

ans = deque([N])
for i, c in zip(range(N - 1, -1, -1), S_list):
    # print("i, c", i, c)
    if c == "L":
        ans.append(i)
    else:
        ans.appendleft(i)
    # print("ans", ans)

print(" ".join(map(str, ans)))
