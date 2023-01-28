def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
A = nextIntList()

A.sort()

# print(A)

max_a = A[-1]
min_a = A[0]

part_a = min(min_a, max_a - min_a)
ans_a = min_a
for a in A[1:-1]:
    if min(a, max_a - a) > part_a:
        part_a = min(a, max_a - a)
        ans_a = a

print(max_a, ans_a)