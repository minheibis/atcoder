def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    s = str(input())
    t = str(input())
    len_s = len(s)
    len_t = len(t)
    dp = [["" for _ in range(len_t + 1)] for _ in range(len_s + 1)]
    for i, s_c in enumerate(s):
        for j, t_c in enumerate(t):
            if s_c == t_c:
                dp[i+1][j+1] = dp[i][j] + t_c
            else:
                if len(dp[i+1][j]) > len(dp[i][j+1]):
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
    # print(dp)
    print(dp[len_s][len_t])

solve()