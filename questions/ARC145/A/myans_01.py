from collections import deque
import re

def check_palin(s):
    len_s = len(s)
    # change some letters to x
    for i in range(len_s // 1):
        # can make it half but its ok
        if s[i] == "x":
            s[len_s - 1 - i] == "x"
        elif s[len_s - 1- i] == "x":
            s[i] == "x"

    # check if palin
    if s == s[::-1]:
        return True
    else:
        return False

def solve():
    n = int(input())
    s = list(str(input()))
    len_s = len(s)
    i_list = [i for i in range(len_s)]

    q = deque()
    for r in i_list:
        q.append(r)  ## dequeの右端に要素を一つ追加する。
        (追加した要素に応じて何らかの処理を行う)

        while not (満たすべき条件):
            rm = q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
            (取り除いた要素に応じて何らかの処理を行う)

        (何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。)

    print("No")
    return