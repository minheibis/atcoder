def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MAX_N = 50
MAX_X = 10 ** 4
MAX_A = 100
MAX_B = 50

N, X = nextInts()
A_set = set()
wallet = dict()
MAX_X = 0
for i in range(N):
    A, B = nextInts()
    A_set.add(A)
    wallet[A] = B
    MAX_X += A * B

# print("A_set:", A_set)
# print("wallet:", wallet)

dp = [[[False for _ in range(MAX_X + 1)] for _ in range(MAX_B + 1)] for _ in range(N)]

# 0 Yen is always payable.
dp[0][0][0] = True

for i, a in enumerate(A_set):
    if i != 0:
        # Take the value from MAX_B of previous a, for j == 0
        for x in range(0, X+1):
            dp[i][0][x] = dp[i-1][MAX_B][x]
    for j in range(1, MAX_B + 1):
        # when there is no more coins left for a
        if j > wallet[a]:
            # copy the result of previous j
            for x in range(0, X+1):
                dp[i][j][x] = dp[i][j-1][x]
        # when there is actuall coin
        else:
            for x in range(0, MAX_X + 1):
                # print("a, j, x:", a, j, x)
                dp[i][j][x] = dp[i][j-1][x]
                if x - a >= 0 and dp[i][j-1][x-a]:
                    # print("i, j, x: ", i, j, x)
                    dp[i][j][x] = True
        # print("dp[i][j]: ", i, j, dp[i][j])

# print(dp)

if dp[N-1][MAX_B][X]:
    print("Yes")
else:
    print("No")           