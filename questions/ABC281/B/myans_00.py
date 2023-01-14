def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

S = str(input())

ans = "Yes"
if len(S) == 8:
    for i, s in enumerate(S):
        if i == 0 or i == 7:
            if not s.isupper():
                ans = "No"
        else:
            if not s.isnumeric():
                ans = "No"
            else:
                if i == 1:
                    if s == "0":
                        ans = "No"

else:
    ans = "No"

print(ans)
