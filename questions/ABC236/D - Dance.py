import math

N = int(input()) 
p_num = 2 * N - 1

#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
A = [list(reversed(list(map(int, input().split())))) for l in range(N + 1)]

print(N)
print(A)

def calc_max_score(N, A):
    kumi_list_num = int(math.factorial((2 * N - 1)) / math.factorial(N))
    max_score = 0
    for i in range(kumi_list_num):
        p_rem_list = [i for i in range(p_num)]
        score = 0
        while 1:
            if len(p_rem_list) == 0:
                break
            min_p = p_rem_list[0] # その時点での先頭
            for i, point in enumerate(A[min_p]):
                print("i, point", i, point)
                if min_p == i:
                    continue
                score = score ^ point # 点をかけて、
                p_rem_list.remove(i) # 相手（i）を除く
                p_rem_list = p_rem_list[1:] # 先頭のmin_pを除く
            print("score", score)
        if score > max_score:
            max_score = score
    print(max_score)

calc_max_score(N, A)