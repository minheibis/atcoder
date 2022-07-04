N, X = map(int, input().split())

cost_list = []
for _ in range(N):
    cost_list.append(list(map(int, input().split())))

# print(cost_list)

initial_min = 0
initial_num = 0
ans_cand_list = []
cost_min = float("inf")
for i, cost_tmp in enumerate(cost_list):
    initial_min += (sum(cost_tmp))
    initial_num += 1
    cost_min = min(cost_min, cost_tmp[1])
    ans_min = initial_min + (X - initial_num) * cost_min
    ans_cand_list.append(ans_min)

# print(ans_cand_list)
print(min(ans_cand_list))