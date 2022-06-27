N, X = map(int, input().split())
S = str(input())

X = list(bin(int(X)))

for c in S:
    if c == "U":
        X.pop()
    if c == "L":
        X.append("0")
    if c == "R":
        X.append("1")

print(int("".join(X), 2))
