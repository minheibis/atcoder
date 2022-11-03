def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    H, W = nextInts()
    m = []
    for _ in range(H):
        m.append(list(str(input())))
    ans_list = []
    for i in range(W):
        ans = 0
        for j in range(H):
            if m[j][i] == "#":
                ans += 1
        ans_list.append(ans)
    print(*ans_list)

solve()