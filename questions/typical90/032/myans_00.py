import itertools

n = int(input())

map_run = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp_list = list(map(int, input().split()))
    for j, t in enumerate(tmp_list):
        map_run[j][i] = t # i, jを逆にする

m = int(input())
m_list = []
for _ in range(m):
    a, b = map(int, input().split())
    m_list.append([a-1, b-1])

p_list = [i for i in range(n)]

ans = 10**5
for v in itertools.permutations(p_list, n):
    tmp_score = 0
    for i, tmp_p in enumerate(v):
        # print("i, tmp_p: ", i, tmp_p)
        # print(tmp_score)
        tmp_score += map_run[i][tmp_p]
        if i != n-1:
            for kumi in m_list:
                if (tmp_p == kumi[0] and v[i+1] == kumi[1]) or (tmp_p == kumi[1] and v[i+1] == kumi[0]):
                    tmp_score += 10**5
                    break
        if tmp_score >= 10**5:
            break
    ans = min(ans, tmp_score)

if ans >= 10**5:
    print(-1)
else:
    print(ans)