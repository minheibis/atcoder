# https://atcoder.jp/contests/agc057/submissions/31569160
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 998244353

def euclid(a: int, b: int):
    if a > b:
        a, b = b, a
    ret = []
    while a:
        ret.append(b//a)
        a, b = b%a, a
    return ret
    
def solve():
    X = sorted(nextIntList())
    if len(set(X)) == 1: return 1
    if len(set(X)) == 2: return 2
    da = euclid(X[2] - X[1], X[1] - X[0])
    if len(da) == 1 and da[0] == 1: return 5
    ans, num, prv = 1, 1, 1
    da[-1] -= 1 # to adjust for the last number of the count_a_list
    # print(*da)
    for i in da:
        ans += (num - prv + 1) * i * (i + 1) + (prv - 1) * i * 2
        tmp = num
        num = (num - prv + 1) * (i + 1) + prv - 1
        prv = tmp - prv + 1
        ans %= MOD
        prv %= MOD
        num %= MOD
        # print(ans, num, prv)
    # return ans#+pp
    ans = (ans - (num - prv * 2) + (num + 1) * 2) % MOD # can be this simple?
    return ans


def main():
    t = nextInt()
    for i in range(t):
        print(solve())

if __name__ == '__main__':
    main()