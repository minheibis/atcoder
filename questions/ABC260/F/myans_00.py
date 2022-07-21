def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    s, t, m = map(int, input().split())
    s_v = [set() for _ in range(s)]
    t_u = [set() for _ in range(s+t)]
    # print("s_v:", s_v)
    # print("t_u:", t_u)

    for _ in range(m):
        u, v = map(int, input().split())
        s_v[u-1].add(v-1)
        t_u[v-1].add(u-1)

    # print("s_v:", s_v)
    # print("t_u:", t_u)
    # want to search each of them
    # much easier if I could use bit calculation
    # use AND and count the number
    # if > 2 then answer that pattern, 
    # else if all does not satisfy the condition, answer -1
    for i in range(s, s+t):
        t_1 = t_u[i]
        for j in range(i+1, s+t):
            t_2 = t_u[j]
            # print("i, j, t_1, t_2:", i, j, t_1, t_2)
            t_union = t_1 & t_2
            # print("t_union:", t_union)
            if len(t_union) >= 2:
                ans = " ".join([str(i+1), str(j+1), str(t_union.pop()+1), str(t_union.pop()+1)])
                print(ans)
                return

    print("-1")
    return

solve()