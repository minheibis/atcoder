N = int(input())
# 最初の数字
N_set = set(list(range(2, N*2 + 2)))

# 最初の数字
print(1)
while 1:
    a = int(input())
    if a == 0:
        break
    N_set.remove(a)
    print(N_set.pop())