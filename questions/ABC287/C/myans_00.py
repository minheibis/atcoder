def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = nextInts()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

ans = "Yes"
# パスグラフ (分岐のないツリー)
start = -1
for i, p_list in enumerate(graph):
    if len(p_list) == 1:
        start = i

if start == -1:
    ans = "No"
else:
    visit_set = set()
    visit_set.add(start)

    before = start
    now = graph[start][0]
    while True:
        # print("before, now: ", before, now)
        # print("graph[now]: ", graph[now])
        visit_set.add(now)
        if len(graph[now]) == 2:
            for next_tmp in graph[now]:
                if before != next_tmp:
                    before = now
                    now = next_tmp
                    # print("new before, now: ", before, now)
                    break
        else:
            # print("break")
            break
    # all p
    if len(visit_set) != N:
        ans = "No"

print(ans)