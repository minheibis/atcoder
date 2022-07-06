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
    count_lunluns = [int(i) for i in range(1, 10)]
    front_lunluns = [int(i) for i in range(0, 10)]
    back_lunluns = [int(i) for i in range(0, 10)]
    # print("all_lunluns:", all_lunluns)
    
    len_c = 0
    for i in range(4):
        new_lunluns = [0]
        for a in front_lunluns:
            a = str(a).zfill(2**i)
            for b in back_lunluns:
                b = str(b)
                # print("a,b:", a,b)
                if b[0] == "0" or b[0] == "1":
                    b = b.zfill(2**i)
                elif len(b) != 2**i:                  
                    continue
                if checklunlun(a, b):
                    c = int(a + b)
                    # print("a,b:", a,b)
                    # print("c:", c)
                    if c >= 10**(2**i):
                        count_lunluns.append(c)
                        len_c += 1
                        if len_c > 100000:
                            # count_lunluns = sorted([int(i) for i in count_lunluns])
                            # print(len(count_lunluns))
                            # print("count_lunluns:", count_lunluns)
                            print(int(count_lunluns[k-1]))
                            return
                # if c >= 10**(2**(i + 1) - 1):
                new_lunluns.append(c)
        front_lunluns = sorted(list(set([0] + count_lunluns)))
        back_lunluns = sorted(list(set(new_lunluns)))
        # print("i, front_lunluns:", i, front_lunluns)
        # print("i, back_lunluns:", i, back_lunluns)
        # print("count_lunluns:", count_lunluns)

if __name__ == "__main__":
    main()