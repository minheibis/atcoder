import heapq

def heapsort(iterable):
    heap = []
    for value in iterable:
        heapq.heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]

print(heapsort([
    1, 2, 4, 7, 3, 2
]))