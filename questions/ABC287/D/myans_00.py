from copy import deepcopy
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def check_same_letter(a_i, b_i):
    if a_i == b_i:
        return True
    elif a_i == "?" or b_i == "?":
        return True
    return False

def check_same(a, b):
    same_set = set()
    diff_set = set()
    for i, (a_i, b_i) in enumerate(zip(a, b)):
        if check_same_letter(a_i, b_i):
            same_set.add(i)
        else:
            diff_set.add(i)
    return same_set, diff_set

S = str(input())
T = str(input())
len_T = len(T)

for i in range(-1, len_T):
    if i == -1:
        part_s = deepcopy(S[-len_T:])
        same_set, diff_set = check_same(part_s, T)
    else:
        # check only changes
        # change the i the letter of the string part of S
        if check_same_letter(S[i], T[i]):
            same_set.add(i)
            if i in diff_set:
                diff_set.remove(i)
        else:
            diff_set.add(i)
            if i in same_set:
                same_set.remove(i)
 
    if len(same_set) == len_T:
        print("Yes")
    else:
        print("No")