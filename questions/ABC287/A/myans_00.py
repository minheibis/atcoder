def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


N = nextInt()
yes = 0
no = 0
for i in range(N):
    s = str(input())
    if s == "For":
        yes += 1
    else:
        no += 1

if yes > no:
    print("Yes")
else:
    print("No")