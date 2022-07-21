def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, m, x, t, d = nextInts()
if m >= x:
    print(t)
else:
    print(t - d*(x-m))