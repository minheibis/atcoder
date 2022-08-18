def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

y = nextInt()
s, rm = divmod(y, 4)
if rm <= 2:
    print(s * 4 + 2)
else:
    print((s + 1) * 4 + 2)
