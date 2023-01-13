# https://docs.python.org/ja/3/library/heapq.html

import copy
import heapq
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M, K = nextInts()
A = nextIntList()

heap = copy.deepcopy(A[:M])
heapq.heapify(heap)
ans_list = list()

# print(heap)
# print("heapq.nsmallest(heap, K):", heapq.nsmallest(K, heap))
ans_list.append(sum(heapq.nsmallest(K, heap)))

# thres
for a_out, a_in in zip(A[:N-M], A[M:]):
    # print("a_out, a_in:", a_out, a_in)
    heap.remove(a_out)
    heapq.heappush(heap, a_in)
    ans_list.append(sum(heapq.nsmallest(K, heap)))

print(*ans_list)