def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

mvx, mvy = -1, 1

def solve():
    n = nextInt()
    table = []
    for i in range(n):
        table.append(list(str(input())))

    # print(table)

    for i in range(n * 2 - 1):
        # print("i", i)
        if i <= n:
            x_s = i - 1
            y_s = 0
            x_l = 0
            y_l = i - 1
        else:
            x_s = n - 1
            y_s = i - n
            x_l = i - n
            y_l = n - 1
        while (x_s > x_l):
            # print("x_s, y_s, x_l, y_l: ", x_s, y_s, x_l, y_l)
            if table[y_s][x_s] == "W":
                if table[y_l][x_l] != "L":
                    print("incorrect")
                    return
            elif table[y_s][x_s] == "L":
                if table[y_l][x_l] != "W":
                    print("incorrect")
                    return
            elif table[y_s][x_s] == "D":
                if table[y_l][x_l] != "D":
                    print("incorrect")
                    return
            x_s += mvx
            y_s += mvy
            x_l -= mvx
            y_l -= mvy
            # print("next x_s, y_s, x_l, y_l: ", x_s, y_s, x_l, y_l)
    print("correct")


solve()