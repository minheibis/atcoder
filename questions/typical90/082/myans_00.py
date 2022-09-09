def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 10**9 + 7

def zero_to_n(n):
    len_n = len(str(n))
    ans = 0
    for i in range(len_n):
        min_in_i = 10**i
        if i == len_n - 1:
            max_in_i = n
        else:
            max_in_i = 10**(i + 1) - 1
        ans += (i+1) * (min_in_i + max_in_i) * (max_in_i - min_in_i + 1) // 2
        ans %= MOD
    return ans

def solve():
    L, R = nextInts()
    ans = (zero_to_n(R) - zero_to_n(L-1)) % MOD
    print(ans)

solve()

