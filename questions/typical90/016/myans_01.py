def solve():
    n = int(input())
    a, b, c = map(int, input().split())

    ans = 10000
    for x in range(10000):
        for y in range(10000-x):
            a_b_sum = x * a + y * b
            z, rem = divmod(n - a_b_sum, c)
            if rem == 0 and z >= 0:
                tmp_ans = x + y + z
                if tmp_ans < ans:
                    ans = tmp_ans
                    print("x, y, z:", x, y, z)
                    print("sum", a * x + b * y + c * z)
    print(ans)

solve()