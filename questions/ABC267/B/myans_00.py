from tokenize import Triple


def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    pins = list(str(input()))
    row_list = [False for _ in range(7)]
    if pins[0] == "1":
        print("No")
    else:
        if pins[6] == "1":
            row_list[0] = True
        if pins[3] == "1":
            row_list[1] = True
        if pins[7] == "1" or pins[1] == "1":
            row_list[2] = True
        if pins[4] == "1" or pins[0] == "1":
            row_list[3] = True
        if pins[8] == "1" or pins[2] == "1":
            row_list[4] = True
        if pins[5] == "1":
            row_list[5] = True
        if pins[9] == "1":
            row_list[6] = True
        # print("row_list:", row_list)

        split_flag = False
        for i in range(len(row_list)-2):
            if row_list[i] == True:
                # print("start i:", i)
                for j in range(i+1, len(row_list)-1):
                    if row_list[j] == False:
                        # print("mid j:", j)
                        for k in range(j+1, len(row_list)):
                            if row_list[k] == True:
                                # print("end k:", k)
                                split_flag = True


        if split_flag:
            print("Yes")
        else:
            print("No")

solve()