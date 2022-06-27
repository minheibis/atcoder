n = int(input())

ans = []
for bit in range(2**n):
    res = ""
    tmp = 0
    for i in range(n):
        if (bit >> i) & 1:
            res += "("
            tmp += 1
        else:
            res += ")"
            tmp -= 1
        if tmp < 0:
            break
    if tmp == 0:
        ans.append(res)

ans.sort()

for res in ans:
    print(res)