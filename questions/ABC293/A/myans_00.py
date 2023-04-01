def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

S = str(input())

ans = ""
for i, c in enumerate(S):
    if i % 2 == 0:
        ans += S[i+1]
        ans += S[i]


print(ans)