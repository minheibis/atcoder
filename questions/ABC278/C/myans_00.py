from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

fol_dict = defaultdict(set)

n, q = nextInts()
for i in range(q):
    t, a, b = nextInts()
    if t == 1:
        fol_dict[a].add(b)
    elif t == 2:
        if b in fol_dict[a]:
            fol_dict[a].remove(b)
    elif t == 3:
        if (b in fol_dict[a]) and (a in fol_dict[b]):
            print("Yes")
        else:
            print("No")
