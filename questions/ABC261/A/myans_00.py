import numpy as np

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

boxs = np.zeros(100)
l1, r1, l2, r2 = nextInts()
boxs[l1: r1] += 1
boxs[l2: r2] += 1

print(sum(boxs == 2.0))