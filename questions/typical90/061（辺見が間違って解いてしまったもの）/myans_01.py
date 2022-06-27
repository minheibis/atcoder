from collections import deque
q = int(input())
deq = deque()
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        # 計算量:O(1)
        deq.appendleft(x)
    elif t == 2:
        # 計算量:O(1)
        deq.append(x)
    elif t == 3:
        # 計算量:O(n)
        print(deq[x-1])