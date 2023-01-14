from collections import defaultdict
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
c_dict = defaultdict(int)
a = nextIntList()
for i, x in enumerate(a):
    c_dict[i + 1] += x
q = nextInt()

for _ in range(q):
    query = nextIntList()
    # print("c_dict: ", c_dict)
    # print("query: ", query)
    if query[0] == 1:
        x = query[1]
        c_dict = defaultdict(lambda: x)
    elif query[0] == 2:
        i = query[1]
        y = query[2]
        c_dict[i] += y
        # c_dict[i] = c_dict[i] + x
    elif query[0] == 3:
        i = query[1]
        print(c_dict[i])
