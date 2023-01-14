def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ans[0:N])