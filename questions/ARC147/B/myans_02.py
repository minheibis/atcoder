def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    P = nextIntList()
    # print("start: ", P)


    # あとは交換していく
    ans_num = 0
    ans_list = []
    for _ in range(N):
        count = 0
        for i in range(0, N-1):
            if (P[i]%2 != (i+1)%2) and (P[i+1]%2 != (i+2)%2):
                P[i+1], P[i] = P[i], P[i+1]
                # print(P)
                ans_num += 1
                ans_list.append(("A", i+1))
                count += 1

        for i in range(0, N-1):
            if i < N-2 and (P[i] > P[i+2]) and (P[i]%2 == P[i+2]%2):
                P[i+2], P[i] = P[i], P[i+2]
                # print(P)
                ans_num += 1
                ans_list.append(("B", i+1))
                count += 1

        for i in range(0, N-1):
            if i < N-2 and (P[i] > P[i+2]):
                P[i+2], P[i] = P[i], P[i+2]
                # print(P)
                ans_num += 1
                ans_list.append(("B", i+1))
                count += 1
                break
        if count == 0:
            break

    # print("last:", P)
    print(ans_num)
    for ans in ans_list:
        print(ans[0], ans[1])

solve()