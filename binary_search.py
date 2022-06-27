def binary_search(N, A, x):
    l = 0
    r = N - 1
    while r - l >= 0:
        m = (l + r) // 2
        if A[m] == x:
            return m
        if A[m] < x:
            l = m + 1
        if A[m] > x:
            r = m - 1
    return -1