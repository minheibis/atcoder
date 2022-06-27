from collections import deque

N = int(input())
A = []
for i in range(2 * N):
    if i < (2 * N - 1):
        a = list(map(int, input().split()))
    else:
        a = []
    A.append([-1] * (i + 1) + a)

#print("A", A)

n_list = [i for i in range(2 * N)]

deq_score_and_n = deque([(0, n_list)])

m = 0
for i in range(N):
    deq_score_and_n_new = deque()
    for score_and_n in deq_score_and_n:
        #print("score_and_n", score_and_n)
        old_score = score_and_n[0]
        old_n_list = score_and_n[1]
        #print("old_n_list", old_n_list)
        n_0 = old_n_list[0]
        new_list = old_n_list[1:]
        for j, n_1 in enumerate(new_list):
            new_score = old_score ^ A[n_0][n_1]
            deq_score_and_n_new.append((new_score, new_list[0:j] + new_list[j+1:]))
            if len(old_n_list) == 2: # ついでに判定してしまう工夫が必要だった。
                if new_score > m:
                    m = new_score
    deq_score_and_n = deq_score_and_n_new
    #print("deq_score_and_n", deq_score_and_n)

print(m)
