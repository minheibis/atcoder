H, W = map(int, input().split())


def lis(n, A):
    L = [0 for i in range(n + 1)]
    L[0] = A[0]
    length = 1
    for i in range(1, n):
        # print(L)
        if L[length - 1] < A[i]:
            L[length] = A[i]
            length += 1
        else:
            index = bisect.bisect_left(L, A[i], 0, length)
            L[index] = A[i]
    # print(L)
    return length