from math import floor, ceil, sqrt

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

A, B = nextInts()
just = (A / (2 * B)) ** (2/3)
# print(just)
low = floor(just)
high = ceil(just)

def calc_ans(x):
    return B * (x - 1) + A / sqrt(x)

if low == 0:
    ans = calc_ans(high)
else:  
    low_ans = calc_ans(low)
    high_ans = calc_ans(high)
    ans = min(low_ans, high_ans)
print(ans)