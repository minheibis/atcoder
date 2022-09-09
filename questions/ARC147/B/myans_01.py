def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    P = nextIntList()
    print(P)

    # 偶奇をそろえて


    # あとは交換していく
    ans_num = 0
    ans_list = []
    for _ in range(N):
        count = 0
        for i in range(0, N-2):
            if P[i] > P[i+2]:
                P[i+2], P[i] = P[i], P[i+2]
                print(P)
                ans_num += 1
                ans_list.append({"B": i+1})
                count += 1
        if count == 0:
            break

    for _ in range(N):
        count = 0
        for i in range(0, N-1):
            if P[i] > P[i+1]:
                P[i+1], P[i] = P[i], P[i+1]
                print(P)
                ans_num += 1
                ans_list.append({"A": i+1})
                count += 1
        if count == 0:
            break

    print(P)
    print(ans_num)
    print(ans_list)


solve()