from collections import deque

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(list(map(int, input().split())))
q_list = list(input())

def f(N_list, q_list):
    N_deq = deque()
    q_deq = deque()
    reach_y_set = set()
    for i, (p_list, q) in enumerate(zip(N_list, q_list)):
        if i == 0:
            N_deq.append(p_list)
            q_deq.append(q)
            continue            
        if p_list[0] < N_deq[0][0]:
            N_deq.appendleft(p_list)
            q_deq.appendleft(q)
        else:
            N_deq.append(p_list)
            q_deq.append(q)
        p_list = N_deq.pop()
        q = q_deq.pop()
        x = p_list[0]
        y = p_list[1]
        print(i, q, x, y)
        if y not in reach_y_set:
            # リーチじゃないとき
            if q == "R":
                # 右むきならリーチ
                reach_y_set.add(y)
        else:
            # すでにリーチの時
            if q == "L":
                print("Yes")
                return
    p_list = N_deq.popleft()
    q = q_deq.popleft()
    x = p_list[0]
    y = p_list[1]
    print(i, q, x, y)
    if y not in reach_y_set:
        # リーチじゃないとき
        if q == "R":
            # 右むきならリーチ
            reach_y_set.add(y)
    else:
        # すでにリーチの時
        if q == "L":
            print("Yes")
            return
    print("No")
    return

f(N_list, q_list)