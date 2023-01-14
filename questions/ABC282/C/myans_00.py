def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
S = list(str(input()))

flag_in = False
ans = ""
for i, c in enumerate(S):
    if c == "\"":
        if flag_in:
            flag_in = False
        else:
            flag_in = True
    if flag_in == False:
        if c == ",":
            S[i] = "."

S = "".join(S)

print(S)