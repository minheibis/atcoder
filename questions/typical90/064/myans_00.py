import numpy as np

n, q = map(int, input().split())
a_list = np.array(list(map(int, input().split())))

q_list = []
for _ in range(q):
    q_list.append(list(map(int, input().split())))
q_list = np.array(q_list)

ans = 0
for i in range(1, n):
    ans += abs(a_list[i] - a_list[i-1])

for i in range(q):
    l, r, v = q_list[i][0], q_list[i][1], q_list[i][2]
    if l-1 > 0:
        l_gap_b = abs(a_list[l-1] - a_list[l-2])
    if r < n:
        r_gap_b = abs(a_list[r-1] - a_list[r])
    a_list[l-1:r] += v
    if l-1 > 0:
        l_gap_a = abs(a_list[l-1] - a_list[l-2])
        ans += (l_gap_a - l_gap_b)
    if r < n:
        r_gap_a = abs(a_list[r-1] - a_list[r])
        ans += (r_gap_a - r_gap_b)
    # print(a_list)
    print(ans)
