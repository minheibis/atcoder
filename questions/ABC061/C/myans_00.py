def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, k = nextInts()
h = list()
for _ in range(n):
    a, b = nextInts()
    k -= b
    if k <= 0:
        print(a)
        break
