N, X = map(int, input().split())
S = str(input())

# まずは、LUあるいはRUを取り除く
S_new = []
for c in S:
    if c == "U" and len(S_new) > 0 and (S_new[-1] == "L" or S_new[-1] == "R"):
        S_new.pop()
    else:
        S_new.append(c)

# print(S_new)

# その後実際にシミュレートする。

for c in S_new:
    if c == "U":
        X //= 2
    elif c == "L":
        X *= 2
    elif c == "R":
        X *= 2
        X += 1

print(X)