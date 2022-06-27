import queue

N, Q = map(int, input().split())
e_list = [[] for i in range(N)] # 道を格納するためのリストを用意
for i in range(N - 1):
    a, b = map(int, input().split())
    e_list[a-1].append(b-1)
    e_list[b-1].append(a-1)

# print("e_list:", e_list)

# 各街の偶奇を計算しておく
que = queue.Queue()
color_list = [-1 for i in range(N)]

color_list[0] = 0
que.put(0)

while not que.empty():
    town_now = que.get()
    #print("town_now: ", town_now)
    #print("color_list: ", color_list)
    for town_next in e_list[town_now]:
        if color_list[town_next] == -1:
            #print("town_next: ", town_next)
            #print("color_list[town_now]:", color_list[town_now])
            color_list[town_next] = 1 ^ color_list[town_now] # XORのビット演算
            que.put(town_next)
#print("color_list:", color_list)

# クエリに答える
for _ in range(Q):
    a, b = map(int, input().split())
    if color_list[a-1] == color_list[b-1]:
        print("Town")
    else:
        print("Road")