n = int(input())
a_list = list(map(int, input().split()))
rui_list = [0, 0, 0, 0]

ans = 0
for a in a_list:
    rui_list[0] += 1
    ans += sum(rui_list[4 - a:4])
    rui_list[a:4] = rui_list[0:4 - a]
    rui_list[0:a] = [0 for _ in list(range(a))]
    # print("rui_list, ans:", rui_list, ans)
    
print(ans)