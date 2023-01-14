def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
MAX_INT = 2 * 10**5

N = nextInt()
A = nextIntList()

change_map = dict()
for i in range(1, MAX_INT + 1):
    change_map[i] = i

ans = 0
for i in range(N//2):
    f = change_map[A[i]]
    b = change_map[A[-(i + 1)]]
    print("A[i], A[-(i + 1)]: ", A[i], A[-(i + 1)])
    print("f, b: ", f, b)
    if f != b:
        change_map[f] = b
        ans += 1

print(ans)
