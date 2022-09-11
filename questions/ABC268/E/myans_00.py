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
        # tmp_num = (p_list[i] - n_list[i]) % N
        # d[min(tmp_num, abs(N - tmp_num))] += 1

    print("d: ", d)
    mv = max(d, key=d.get)
    
    print("mv:", mv)
    ans = 0
    for i in range(N):
        tmp_num = (p_list[(i - mv) % N] - n_list[i]) % N
        print(i, min(tmp_num, abs(N - tmp_num)))
        ans += min(tmp_num, abs(N - tmp_num))

    print(ans)

solve()