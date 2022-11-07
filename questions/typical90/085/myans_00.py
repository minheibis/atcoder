from math import sqrt

def divisors(n):
    divisors = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def solve():
    K = int(input())
    ans = 0
    for a in divisors(K):
        for b in divisors(K // a):
            c = K // (a * b)
            if a <= b <= c:
                ans += 1
    print(ans)

solve()