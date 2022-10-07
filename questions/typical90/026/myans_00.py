from collections import deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N = nextInt()
    g = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = nextInts()
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    has_visited = set()
    ans_1 = []
    ans_2 = []
    deq = deque()
    deq.append((0, True))
    while len(deq) != 0:
        now, adj_flag = deq.pop()
        has_visited.add(now)
        if adj_flag:
            ans_1.append(now)
            adj_flag = False
        else:
            ans_2.append(now)
            adj_flag = True
        for next in g[now]:
            if next not in has_visited:
                deq.append((next, adj_flag))

    half_ans = []
    if len(ans_1) > len(ans_2):
        ans = ans_1
    else:
        ans = ans_2
    for a in ans[0:N//2]:
        half_ans.append(a+1)
    print(*half_ans)

solve()