def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
A = nextIntList()

def my_gcd(x, y):
    r = x % y
    if r != 0:
        return my_gcd(y, r)
    else:
        return y

def my_gcd_list_no_i(x_list, i):
    if i == 0:
        start = 1
    else:
        start = 0
    x = x_list[start]
    for j, y in enumerate(x_list):            
        if j == start:
            continue
        if i == j:
            continue
        # print("x, y: ", x, y)
        x = my_gcd(x, y)
        # print("x: ", x)
    return x

ans = 1
for i, a in enumerate(A):
    tmp_ans = my_gcd_list_no_i(A, i)
    ans = max(ans, tmp_ans)
    # print(i, ans)

print(ans)