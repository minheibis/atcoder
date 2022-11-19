def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, X = nextInts()
P_list = nextIntList()
print(P_list.index(X) + 1)