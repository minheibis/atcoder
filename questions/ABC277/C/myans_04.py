def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

from collections import defaultdict, deque

list_dict = defaultdict(list)
N = nextInt()
for i in range(N):
    A, B = nextInts()
    list_dict[A].append(B)
    list_dict[B].append(A)

# print(list_dict)

deq = deque()
visited = set()
start = 1
ans = start
deq.append(start)
visited.add(start)

while deq:
    now = deq.pop()
    ans = max(ans, now)
    next_list = list_dict[now]
    for next in next_list:
        if next not in visited:
            deq.append(next)
            visited.add(next)

print(ans)