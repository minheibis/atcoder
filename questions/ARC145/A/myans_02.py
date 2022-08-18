def solve():
    n = int(input())
    s = str(input())
    if s == "BA":
        print("No")
        return
    s = list(s)
    len_s = len(s)
    a_flag = False
    b_flag = False
    for i in range(len_s // 2):
        # can make it half but its ok
        if s[len_s - 1 - i] == "A":
            a_flag = True
        if s[i] == "B":
            b_flag = True
        if s[i] != s[len_s - 1 - i]:
            if a_flag == False and b_flag == False:
                print("No")
            else:
                print("Yes")
            return
    print("Yes")
    return

solve()