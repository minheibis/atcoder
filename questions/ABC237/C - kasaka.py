from collections import deque

S = deque(str(input()))
S_rev = reversed(S)

for i in S_rev:
    if i == "a":
        S = S[:-1]
    else:
if S == S[::-1]:
    print("Yes")
else:
    print("No")

