from collections import defaultdict
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


N, Q = nextInts()
boxes = defaultdict(list)
balles = defaultdict(int)

for i in range(1, N + 1):
    boxes[i].append(i)
    balles[i] = i

ball_sum = N
for _ in range(Q):
    q = nextIntList()
    if q[0] == 1:
        x = q[1]
        y = q[2]
        # put y into x
        for ball in boxes[y]:
            balles[ball] = x
        boxes[x] += boxes[y]
        boxes[y] = list()
    elif q[0] == 2:
        x = q[1]
        # put a ball_sum into x
        ball_sum += 1
        boxes[x].append(ball_sum)
        balles[ball_sum] = x
    elif q[0] == 3:
        x = q[1]
        # call num of the box which ball x is in
        print(balles[x])
    # print("boxes: ", boxes)
    # print("balles: ", balles)