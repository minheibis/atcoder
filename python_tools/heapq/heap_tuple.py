from heapq import heappush, heappop

h = []
heappush(h, (5, "a"))
heappush(h, (7, "b"))
heappush(h, (1, "c"))
heappush(h, (3, "d"))

for i in range(len(h)):
    print(heappop(h))