import itertools

N, Y = map(int, input().split())

def calc(N, Y):
    for x in range(0, N + 1):
        for y in range(0, N + 1 - x):
            z = N - x - y
            #print(x, y, z)
            if z < 0:
                break
            money_sum = x * 10000 + y * 5000 + z * 1000
            if money_sum == Y:
                print(x, y, z)
                #print(money_sum)
                return
    print(-1, -1, -1)
    return

calc(N, Y)