def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

H, M = nextInts()

while True:
    H_str = format(H, '02')
    M_str = format(M, '02')
    h = int(H_str[0] + M_str[0])
    m = int(H_str[1] + M_str[1])
    # print(H, M)
    # print(h, m)
    if (0 <= h <= 23) and (0<= m <= 59):
        break
    M += 1
    M %= 60
    if M == 0:
        H += 1
        H %= 24

print(H, M)