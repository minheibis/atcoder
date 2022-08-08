def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
c_list = [i for i in range(n)]
p_list = nextIntList()
p_list = [(i-1) for i in p_list]

ans = 0
c_now = n-1
while True:
    c_now = p_list[c_now-1]
    ans += 1
    if c_now == 0:
        break
print(ans)