from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

d = defaultdict(int)
n = int(input())
for _ in range(n):
    s = str(input())
    d[s] += 1
    if d[s] == 1:
        print(s)
    else:
        print("{}({})".format(s, d[s] - 1))