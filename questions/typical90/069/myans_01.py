MOD = 10**9 + 7

def solve():
    N, K = map(int, input().split())
    if N == 1:
        ans = K
    else:
        ans = (K * (K-1) * pow(K-2, N-2, MOD)) % MOD
    print(ans)

solve()