def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

K, N, M = nextInts()
A = nextIntList()

L = N * M

list_sum = []
a_sum = 0
for i, a in enumerate(A):
    a_sum += a * M
    list_sum.append(round(a_sum / N) * N)

# print("list_sum: ", list_sum)

ans_list = []
now = list_sum[0]
ans_list.append(now // N)
for next in list_sum[1:]:
    ans_list.append((next - now) // N)
    now = next

print(*ans_list)