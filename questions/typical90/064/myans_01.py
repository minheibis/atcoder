def solve():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))

    q_list = []
    for _ in range(q):
        q_list.append(list(map(int, input().split())))

    a_diff = []
    for i in range(1, n):
        a_diff.append(a_list[i] - a_list[i-1])

    ans = 0
    for diff in a_diff:
        ans += abs(diff)

    for i in range(q):
        # print("before: ", i, a_diff)
        l, r, v = q_list[i][0], q_list[i][1], q_list[i][2]
        if l >= 2:
            ans -= abs(a_diff[l-2])
            a_diff[l-2] += v
            ans += abs(a_diff[l-2])
        if r <= n - 1:
            ans -= abs(a_diff[r-1])
            a_diff[r-1] -= v
            ans += abs(a_diff[r-1])
        # print("after:", i, a_diff)        
        print(ans)

solve()