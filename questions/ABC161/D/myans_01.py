# lun-lun number is at least a combnination of lunlun numbers
# can search all lun-lun number until it is over 10**5
# caution that 0 starting number is lun-lun but does not count


def checklunlun(a, b):
    if abs(int(a[-1]) - int(b[0])) <= 1:
        return True
    else:
        return False

def main():
    k = int(input())
    count_lunluns = set([i for i in range(1, 10)])
    front_lunluns = set([i for i in range(0, 10)])
    back_lunluns = set([i for i in range(0, 10)])
    # print("all_lunluns:", all_lunluns)
    
    len_c = 0
    for i in range(4):
        new_lunluns = set()
        for a in front_lunluns:
            a = str(a)
            a = a.zfill(2**i)
            for b in back_lunluns:
                b = str(b)
                b = b.zfill(2**i)
                if checklunlun(a, b):
                    c = a + b
                    # print("a,b:", a,b)
                    # print("c:", c)
                    if int(c) >= 10**(2**i):
                        count_lunluns.add(int(c))
                        len_c += 1
                        if len_c > 200000:
                            # count_lunluns = sorted([int(i) for i in count_lunluns])
                            # print(len(count_lunluns))
                            print("sorted(list(count_lunluns)):", sorted(list(count_lunluns)))
                            print(sorted(list(count_lunluns))[k-1])
                            return
                    new_lunluns.add(c)
        front_lunluns = front_lunluns | new_lunluns
        back_lunluns = new_lunluns
        print("i, front_lunluns:", i, front_lunluns)
        print("i, back_lunluns:", i, back_lunluns)
        print("count_lunluns:", count_lunluns)

if __name__ == "__main__":
    main()