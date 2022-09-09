import numpy as np

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N, M = nextInts()
    A = np.array(nextIntList())
    A_M_arry = A[0:M]
    range_array = np.array(list(range(1, M+1)))

    dot_array = A_M_arry * range_array
    # print("A_M_arry:", A_M_arry)
    # print("dot_array:", dot_array)
    # print("ans:", sum(dot_array))
    sum_A_M_arry = sum(A_M_arry)

    ans = sum(dot_array)
    tmp_ans = ans

    for i in range(1, N-M+1):
        tmp_ans -= sum_A_M_arry
        tmp_ans += (M * A[i+M-1])
        # print("tmp_ans:", tmp_ans)
        
        ans = max(ans, tmp_ans)
        sum_A_M_arry -= A[i-1]
        sum_A_M_arry += A[i+M-1]

    print(ans)

solve()