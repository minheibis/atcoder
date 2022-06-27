N = int(input()) 
#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
A = [list(reversed(list(map(int, input().split())))) for l in range(N + 1)]

print(N)
print(A)

p_num = 2 * N - 1
p_rem_list = [i for i in range(p_num)]
max_score = 0

A_tmp = A.copy()
for i in p_num:
    if i not in p_rem_list:
        continue
    min_p = p_rem_list[0]
    for j in A_tmp[min_p]:

        # 使われた相手を除く 
        p_rem_list.remove(j)
        A_tmp = A_tmp[:j] + A_tmp[j+1:]
    p_rem_list = p_rem_list[1:] # 先頭のiを除く

print(max_score)