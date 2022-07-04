n = int(input())
c_list = list(map(int, input().split()))
min_c = min(c_list)
loop_num = str([i for i, x in enumerate(c_list) if x == min_c][-1] + 1)
keta = n // min_c
start_keta = keta

ans = "0"
for i in range(start_keta):
    if keta != start_keta:
        if ans == "0":
            ans = loop_num
        else:
            ans += loop_num
        n -= min_c
        keta -= 1
    else:
        for j, c in zip(range(9, 0, -1), c_list[::-1]):
            if (n - c) // min_c >= keta - 1:
                if ans == "0":
                    ans = str(j)
                else:
                    ans += str(j)
                n -= c
                keta -= 1
                break

print(ans)