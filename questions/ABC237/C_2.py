from collections import deque
import copy

S = deque(str(input()))
# print(S)
S_2 = copy.deepcopy(S)

r_count = 0
len_S = len(S)
while (len_S > 0) and (S_2[0] == "a"):
    S_2.pop()
    len_S -= 1
    r_count += 1
while (len_S > 0) and (S.popleft() == "a") and r_count > 0:
    S_2.popleft()
    len_S -= 1
    r_count -= 1

S = "".join(S_2)

if S == S[::-1]:
    print("Yes")
else:
    print("No")
