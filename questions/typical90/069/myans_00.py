MOD = 10**9 + 7

# when n_edge <= 4
def calc_edge_ans(k, n_edge):
    edge_ans = 1
    for i in range(n_edge):
        print("k - i:", k - i)
        edge_ans *= max(k - i, 0)
        edge_ans %= MOD
    return edge_ans

def solve():
    n, k = map(int, input().split())
    if n <= 4:
        ans = calc_edge_ans(k, n)
    else:
        edge_ans = calc_edge_ans(k, 4)
        ans = (k-4)**(n-4)
        ans %= MOD
        ans *= edge_ans
        ans %= MOD
    print(ans)

solve()