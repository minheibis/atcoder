def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)
    c = [abs(num[0] - num[1]) for num in zip(a, b)]
    print(sum(c))    

solve()