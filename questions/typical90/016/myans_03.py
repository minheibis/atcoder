def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, new_b, new_a = extgcd(b, a % b)
    new_b -= a // b * new_a
    return g, new_a, new_b

def solve():
    n = int(input())
    a, b, c = sorted(map(int, input().split()))
    print("a, b, c:", a, b, c)

    ans = 10000
    g, new_a, new_b = extgcd(a, b)
    print("g, new_a, new_b:", g, new_a, new_b)
    for z in range(int(10000 // c)):
        sum_a_b = n - z * c
        mul_g, rem = divmod(sum_a_b, g)
        if rem == 0:
            x = new_a * mul_g
            y = new_b * mul_g
            ans = min(ans, x + y + z)
            print("x, y, z, ans:", x, y, z, ans)
    print(ans)

solve()