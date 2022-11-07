def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 10**5
def calc(x):
    y = 0
    x_c = x
    while x_c > 0:
        x_c, y_c = divmod(x_c, 10)
        y += y_c
    return (x + y) % MOD

def solve():
    N, K = nextInts()
    start_list = [N]
    routine_list = list()
    count = 0
    routine_flag = False

    # find until routine
    while True:
        N = calc(N)
        count += 1
        if count == K:
            break
        if routine_flag:
            if N == routine_list[0]:
                break
            routine_list.append(N)
        else:
            if N in start_list:
                routine_flag = True
                routine_list.append(N)
            start_list.append(N)
    if count == K:
        print(N)
        return

    # calc routine
    rem = K - count
    pos = rem % len(routine_list)
    print(routine_list[pos]) 

solve()