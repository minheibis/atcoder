def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
A = nextIntList()

not_called = set([i for i in range(1, N+1)])
called = set()

for i, a in enumerate(A):
    num = i + 1
    if num in not_called:
        called.add(a)
        not_called.discard(a)

ans = list(not_called)
ans.sort()

print(len(ans))
print(*ans)