# https://miaoued.net/archives/2224
def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
result = 0
for i in range(1, 16):
    start = int("1" * i)
    if start > N:
        break
    else:
        result += 1
    bottom = start
    top = start
    
    while True:
        bottom *= 10
        top = (top + 1) * 10 - 1

        if N < bottom:
            break

        result += min(N, top) - bottom + 1
    
print(result)