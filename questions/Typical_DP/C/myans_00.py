def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def win_p_q(rp, rq):
    win_p = 1 / (1 + 10**((rp-rq)/400))
    win_q = 1 - rp
    return win_p, win_q

def main():
    k = nextInt()
    rates = []
    for i in range(k):
        rates.append(nextInt())
    dp = [[1 for _ in range(2**k)] for _ in range(k)]
    for i in range(k):
        for j in range(2**k):
            tmp = 0
            # 対戦する人を割り出す必要がある。

            for aite in range(f, f+2**(i-1)):
                # 勝つ確率
                tmp += dp[i][j] * dp[i][aite]*pwin(rates[j], rates[aite])                

    # 計算するところ

    for  in dps[]:
        print(win_prob)

if __name__ == "__main__":
    main()