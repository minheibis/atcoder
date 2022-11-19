def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
set_list = [set([1])]
for i in range(N):
    # print(set_list)
    A, B = nextInts()
    in_set = False
    new_set = None
    for set_now in set_list:
        if A in set_now:
            set_now.add(B)
            in_set = True
        if B in set_now:
            set_now.add(A)
            in_set = True
        if in_set == False:
            new_set = set([A, B])
            # print(new_set)
    if new_set != None:
        # print(new_set)
        set_list.append(new_set)

for set_now in set_list:
    if 1 in set_now:
        ans = max(set_now)

print(ans)