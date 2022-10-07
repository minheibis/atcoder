def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()

    if N == 0:
        print("0")
    else:
        bin_N = format(N, 'b')
        cont_0 = 0
        bin_set = set()
        bin_set.add("0")
        bin_set.add("1")
        # print("bin_N: ", bin_N)
        # print(int(bin_N, 2))
        for a in bin_N[1: ]:
            # # print("a:", a)
            if a == "0":
                cont_0 += 1
            elif a == "1":
                new_bin_set = set()
                # print("bin_set: ", bin_set)
                for bin_num in bin_set:
                    # # print("bin_num: ", bin_num)
                    # # print("cont_0: ", cont_0)
                    bin_num_ser_0 = bin_num + ("0" * cont_0)
                    # # print("bin_num_ser_0: ", bin_num_ser_0)
                    new_bin_set.add(bin_num_ser_0 + "0")
                    new_bin_set.add(bin_num_ser_0 + "1")
                bin_set = new_bin_set
                cont_0 = 0
        for bin_num in sorted(bin_set):
            bin_num += ("0" * cont_0)
            # print("bin_num: ", bin_num)
            print(int(bin_num, 2))

solve()