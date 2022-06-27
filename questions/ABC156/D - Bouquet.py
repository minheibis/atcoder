from functools import reduce

M = 10**9 + 7
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(lambda x, y: x * y % M, range(n, n - r, -1), 1)
    denom = reduce(lambda x, y: x * y % M, range(1, r + 1), 1)
    return numer * pow(denom, M - 2, M) % M

