# https://blog.hamayanhamayan.com/entry/2019/04/28/085936

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

def my_gcd_list(x_list):
    x = x_list[0]
    gcd_list = [x]
    for y in x_list[1:]:
        x = my_gcd(x, y)
        gcd_list.append(x)
    return gcd_list

gcd_list_forward = my_gcd_list(A)
gcd_list_backward = my_gcd_list(list(reversed(A)))

ans = 1
max_i = len(A) - 1
for i, a in enumerate(A):
    if i == 0:
        tmp_ans = gcd_list_backward[-2]
    elif i == max_i:
        tmp_ans = gcd_list_forward[-2]
    else:
        forward = gcd_list_forward[i - 1]
        backward = gcd_list_backward[- (i + 2)]
        tmp_ans = my_gcd(forward, backward)
        # print(forward, backward)
    ans = max(ans, tmp_ans)

# print(gcd_list_forward)
# print(gcd_list_backward)
print(ans)