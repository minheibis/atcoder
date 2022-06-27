import numpy as np
from collections import deque

def main():
    N, M = map(int, input().split())
    list_a = np.flip(np.array(list(map(int, input().split()))))
    list_c = np.flip(np.array(list(map(int, input().split()))))
    #print(list_a)
    #print(list_c)

    deq_b = deque()

    tmp_list_c = list_c[0:N+1]
    for i in range(M + 1):
        #print("i:", i)
        #print("tmp_list_c:", tmp_list_c)
        # 差分を引き算する
        mul_val = tmp_list_c[0] // list_a[0]
        list_c[i:i+N+1] = tmp_list_c - (list_a * mul_val)
        deq_b.appendleft(mul_val)
        # 更新する
        tmp_list_c = list_c[i + 1: i + N + 2]
    
    print(*list(deq_b))
    return

main()