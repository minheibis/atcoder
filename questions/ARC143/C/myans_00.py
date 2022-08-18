def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, x, y = nextInts()
a_list = nextIntList()

ans = "Second"
xy = x + y
for a in a_list:
    rem = a % xy
    print("x, y, rem", x, y, rem)
    if rem >= x and x <= y:
        ans = "First"
print(ans)