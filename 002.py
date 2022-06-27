N = int(input())

# N個の全部の括弧を表示するケース
def one(N):
    half = N / 2
    ans = "(" * half + ")" * half
    print(ans)

# 分割がないケース
def no_split(N, def_n):
    before = 
    print(before)
    one(N)
    print(after)
    middle = N - 2
    if middle == 0:
        return 0
    while middle > 0:
        show(middle, N - middle)
        middle -= 2

def show(N):
    no_split(N, 0)
    tmp_N = N - 2
    if tmp_N == 0:
        return 0
    while tmp_N > 0:
        show(tmp_N)
        show(N - tmp_N)
        tmp_N -= 2

if N % 2 == 0:
    print()
elif N == 0:
    print()
else:
    show(N)