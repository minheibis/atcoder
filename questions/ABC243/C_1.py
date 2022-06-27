N = int(input())
N_list = []
for _ in range(N):
    N_list.append(list(map(int, input().split())))
q_list = list(input())
for p_list, q in zip(N_list, q_list):
    p_list.append(q)

def f(N_list):
    #print(N_list)
    N_list = sorted(N_list)
    # print(N_list)
    reach_y_set = set()
    for p_list in N_list:
        x = p_list[0]
        y = p_list[1]
        q = p_list[2]
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

f(N_list)