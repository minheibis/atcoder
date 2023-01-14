def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, T = nextInts()
A = nextIntList()

t = 0
a_sum = sum(A)
T %= a_sum
for i, a in enumerate(A):
    t_old = t
    t += a
    # print("i, a, t_old, t: ", i, a, t_old, t)
    if t > T:
        num = i + 1
        sec = T - t_old
        break

print(num, sec)
