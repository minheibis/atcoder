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

# for(int i=0;i<N;i++) for(int j=0;j<N-2;j++) if(p[j]%2!=p[j+2]%2 && p[j]%2!=j%2) f('B',j);
# for(int i=0;i<N-1;i++)if(p[i]%2!=p[i+1] && p[i]%2==i%2) f('A',i);
# for(int i=0;i<N;i++) for(int j=0;j<N-2;j++) if(p[j]>p[j+2]) f('B',j);

    for _ in range(N):
        # はじにずれているものを、Bで寄せていく
        count = 0
        for i in range(0, N-2):
            if (P[i]%2 != i%2) and (P[i]%2 != P[i+2]%2):
                P[i+2], P[i] = P[i], P[i+2]
                # print(P)
                ans_num += 1
                ans_list.append(("B", i+1))
                count += 1
        if count == 0:
            break

    for _ in range(N):
        # パリティが合わないものを、Aで交換する
        count = 0
        for i in range(0, N-1):
            if (P[i]%2 != P[i+1]) and (P[i]%2 == i%2):
                P[i+1], P[i] = P[i], P[i+1]
                # print(P)
                ans_num += 1
                ans_list.append(("A", i+1))
                count += 1
        if count == 0:
            break

    for _ in range(N):
        # 残りをBで交換する
        count = 0
        for i in range(0, N-2):
            if P[i] > P[i+2]:
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