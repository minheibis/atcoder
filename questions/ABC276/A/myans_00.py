def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

S = str(input())
ans = -1
for i, c in enumerate(S):
    if c == "a":
        ans = i + 1

print(ans)
