MOD = 10**9 + 7

def own_pow(x, n, m):
    ans = 1
    # n が 0 になるまで計算を続ける.
    while n:
        if n & 1: # bit列で考えた時の最後の数字が1の場合は、今保持しているxをかける.
            ans *= x
            ans %= m
        x *= x
        x %= m
        n >>= 1 # bit列を右シフトする.
    return ans

def solve():
    N, K = map(int, input().split())
    if N == 1:
        ans = K
    else:
        ans = (K * (K-1) * own_pow(K-2, N-2, MOD)) % MOD
    print(ans)

solve()