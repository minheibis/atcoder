from collections import Counter
import numpy as np
N = int(input())

s_ar = np.array([list(map(int, list(str(input())))) for l in range(N)])
# print(s_ar)

def main():
    count_list = [0] * 10
    for i in range(10):
        c = Counter(s_ar[:, i])
        # print(c)
        for num, value in c.items():
            add_num = i + (value - 1) * 10
            # print("num, add_num:", num, add_num)
            count_list[num] = max(count_list[num], add_num)
        # print("count_list", count_list)
    # print(count_list)
    print(min(count_list))

main()
