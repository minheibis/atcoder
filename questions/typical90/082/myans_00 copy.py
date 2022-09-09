N = int(input())
S = input()

A, B = [0] * N, [0] * N
for i in range(N):
    if i != 0:
        A[i] = A[i - 1]
        B[i] = B[i - 1]

    if S[i] == 'o':
        A[i] = i + 1
    if S[i] == 'x':
        B[i] = i + 1

ans = 0
for i in range(N):
    # indexをキープしておく。
    ans += min(A[i], B[i])

print(ans)