from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
p_list = list(map(int, input().split()))

K_heap = p_list[0: K]
heapify(K_heap)
print(K_heap[0])

for i in range(K, N):
    if K_heap[0] < p_list[i]:
        heappop(K_heap)
        heappush(K_heap, p_list[i])
    print(K_heap[0])