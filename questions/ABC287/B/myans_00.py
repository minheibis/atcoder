def nextInt(): return int(input())
def nextStr(): return str(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
s_list = []
for _ in range(N):
    s_list.append(nextStr())
t_set = set()
for _ in range(M):
    t_set.add(nextStr())

ans = 0
for s in s_list:
    if s[-3:] in t_set:
        ans += 1
print(ans)
