from queue import Queue
import numpy as np

N, K = map(int, input().split())

s_array_now = list(np.zeros((N, 26)))
for i in range(N):
    s_tmp = list(str(input()))
    for c in s_tmp:
        c_num = ord(c) - ord("a")
        #print(i, c_num)
        s_array_now[i][c_num] = 1

#print("s_array_now:", s_array_now)

ans_que = Queue()
ans_que.put([np.zeros(26), s_array_now])

def slice_list_without_i(target_list, i):
    if i == 0:
        sliced_list = target_list[1:]
    else:
        sliced_list = target_list[0:i] + target_list[i+1:]
    return sliced_list

ans_max = 0
while not ans_que.empty():
    now = ans_que.get()
    s_array_now = now[1]
    print("now:", now)
    for i, add_array in enumerate(s_array_now):
        ans_next = now[0] + add_array
        if ans_next.max() <= K:
            next_s_array = slice_list_without_i(s_array_now, i)
            #print("i, next_s_array: ", i, s_array_now)
            #print("i, next_s_array: ", i, next_s_array)
            ans_que.put([ans_next, next_s_array])  
        else:
            print("now[0]", now[0])
            ans_now = np.count_nonzero(now[0].astype(int) == K)
            ans_max = max(ans_max, ans_now)
print(ans_max)