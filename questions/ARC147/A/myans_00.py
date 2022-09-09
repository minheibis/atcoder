def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

import heapq

def solve():
    N = nextInt()
    A = nextIntList()
    A = [-1 * a for a in A]

    heapq.heapify(A)

    # print(A)
    max_v = -1 * heapq.heappop(A)
    min_v = -1 * max(A) # min
    new_v = max_v % min_v
    if new_v != 0:
        heapq.heappush(A, -new_v)
    else:
        new_v = min_v
    # print("max_v, min_v, new_v:", max_v, min_v, new_v)
    # print("A:", A)
    ans = 1

    while len(A) > 1:
        max_v = -1 * heapq.heappop(A)
        # new_v is next min_v
        # print("before max_v, new_v:", max_v, new_v)
        tmp_new_v = max_v % new_v
        if tmp_new_v != 0:
            heapq.heappush(A, -tmp_new_v)
            new_v = tmp_new_v
        # print("after max_v, new_v:", max_v, new_v)
        # print("A:", A)
        ans += 1
    print(ans)

solve()