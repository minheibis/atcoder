from collections import Counter

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

A = nextIntList()
C = Counter(A)
print(len(C.keys()))