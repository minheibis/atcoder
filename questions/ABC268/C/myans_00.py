from collections import defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    n_list = [i for i in range(N)]
    p_list = nextIntList()

    d = defaultdict(int)
    for i in range(N):
        d[(p_list[i] - n_list[i]) % N] += 1

    # print(d)

    ans = 0
    for i in range(N):
        tmp_ans = d[(i-1) % N] + d[i % N] + d[(i+1) % N]
        ans = max(ans, tmp_ans)
    print(ans)

solve()