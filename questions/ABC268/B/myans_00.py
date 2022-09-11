def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

S = str(input())
T = str(input())
if T.startswith(S):
    print("Yes")
else:
    print("No")