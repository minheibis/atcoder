#https://atcoder.jp/contests/abc257/submissions/32748708

def main():
    n = int(input())
    c = list(map(int, input().split()))

    min_c = min(c)
    d = n // min_c
    rem = n % min_c
    loop_digit = max(i+1 for i, ci in enumerate(c) if ci == min_c)

    head_digit = ""
    for i in range(9, 0, -1):
        di = c[i-1] - min_c
        if di == 0 or i < loop_digit:
          continue
        k = rem // di
        rem %= di
        head_digit += str(i) * k


    print((head_digit + str(loop_digit) * (d))[:d])
    print(head_digit + str(loop_digit) * (d - 1))


            


if __name__ == "__main__":
    main()