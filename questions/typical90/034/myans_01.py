from collections import defaultdict, deque

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# do it by shakutori
def solve():

    N, K = nextInts()
    a_list = nextIntList()

    ans = 0
    len_now = 0
    type_num = 0
    a_deq = deque(a_list)
    partial_deq = deque()
    parital_count = defaultdict(int)

    while a_deq:
        a = a_deq.popleft()
        partial_deq.append(a)
        len_now += 1
        parital_count[a] += 1
        if parital_count[a] == 1:
            type_num += 1
        if type_num <= K:
            ans = max(len_now, ans)
        else:
            a_out = partial_deq.popleft()
            parital_count[a_out] -= 1
            if parital_count[a_out] == 0:
                type_num -= 1
            len_now -= 1
        # print("partial_deq: ", partial_deq)
        # print("len_now: ", len_now)
    print(ans)

solve()