# https://atcoder.jp/contests/arc127/submissions/36767718
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
size = len(n)
ans = 0
count = dict()
count[0] = 0
for i in range(1, size+1):
    if i == size and n[0] == "1":
        for j in range(size):
            if n[j] == "1":
                ans += int(N[])
    else:
        count[i] = 