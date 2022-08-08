def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n, l, r = nextInts()
a_list = nextIntList()

ans = sum(a_list)
y_ans = n * r
ans = min(ans, y_ans)
# print("ans:", ans)

x_ans = 0
for y in range(n-1, -1, -1):
#    y_max_ans = y * r
#    y_ans = min(y_ans, y_max_ans)
    y_ans = y * r

    x_ans += a_list[n-y-1]
    # print("x_ans", x_ans)
    x_max_ans = (n-y) * l
    x_ans = min(x_ans, x_max_ans)

    ans = min(ans, y_ans + x_ans)
    # print("y, n-y-1, y_ans, x_max_ans, x_ans, ans:", y, n-y-1, y_ans, x_max_ans, x_ans, ans)

print(ans)