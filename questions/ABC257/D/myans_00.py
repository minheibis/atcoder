# パワーがあって、入り口と出口がある。
# ってことは、それぞれ計算しておく必要がある。
# 少し工夫したwarshall-floyd法でとく

from math import ceil
N = int(input())

P_list = []
for _ in range(N):
    P_dict = dict()
    P_dict["x"], P_dict["y"], P_dict["P"] = map(int, input().split())
    P_list.append(P_dict)
# print("P_list: ", P_list)

cost = [[float('inf') for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        # print("cost: ", cost)
        # print("cost_now:", ceil(abs(P_list[i]["x"] - P_list[j]["x"]) + abs(P_list[i]["y"] - P_list[j]["y"]) / P_list[i]["P"]))
        # print("P_list[i]: ", P_list[i])
        # print("P_list[j]: ", P_list[j])
        cost[i][j] = ceil((abs(P_list[i]["x"] - P_list[j]["x"]) + abs(P_list[i]["y"] - P_list[j]["y"])) / P_list[i]["P"])

# print("cost: ", cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], max(cost[i][k], cost[k][j]))
# print("cost: ", cost)

ans = float("inf")
for cost_from_one_node in cost:
    ans = min(ans, max([i for i in cost_from_one_node if i > 0]))

print(ans)