def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

S = str(input())
ans = 0
for c in S:
    if c == "v":
        ans += 1
    elif c == "w":
        ans += 2
print(ans)