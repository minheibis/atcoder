def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 998244353

def solve():
    n = nextInt()
    a_list = nextIntList()
    ans = 0
    
    print(ans % MOD)

solve()