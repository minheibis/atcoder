from collections import Counter

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

a = nextIntList()
c = Counter(a)
c_m = c.most_common()
# print(c_m)
if c_m[0][1] == 3 and c_m[1][1] == 2:
    print("Yes")
else:
    print("No")