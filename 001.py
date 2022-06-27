N, L = map(int, input().split())
K = int(input())
A = [0]+list(map(int, input().split()))
A.append(L)

def check(x):
    l = 0
    cnt = 0
    for i in range(N + 1):
        l += A[i+1] - A[i]
        if l >= x:
            cnt += 1
            l = 0
    return cnt >= K + 1

ng = L
ok = -1

while ng - ok > 1:
    mid = (ok + ng) // 2
    if (check(mid)):
        ok = mid
    else:
        ng = mid

print(ok)