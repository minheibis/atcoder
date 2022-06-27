s = int(input())

ans = []
for i in range(s):
    ans_next = [1 for _ in range(i + 1)]
    # print("ans_next init:", ans_next)
    for j, tmp_num in enumerate(ans):
        if j != 0 and j != i:
            ans_next[j] = ans[j] + ans[j-1]
    ans = ans_next
    print(*ans)