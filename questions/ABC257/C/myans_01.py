N = int(input())
S_list = list(map(int, list(str(input()))))
W_list = list(map(int, input().split()))

sw_list = []
for w, s in zip(W_list, S_list):
    sw_list.append([w, s])
sw_list = sorted(sw_list)
# print(sw_list)

f_x = sum(S_list)
# print("f_x:", f_x)
max_ans = f_x

# w_next = sw_list[1][0] # 不要？
for i, ws in enumerate(sw_list):
    if i != len(sw_list) - 1:
        w_next = sw_list[i + 1][0]
    else:
        w_next = -1
    w, s = ws[0], ws[1]
    # print("w_next, w:", w_next, w)
    if s == 1:
        f_x -= 1
    else:
        f_x += 1
    # print("f_x:", f_x)
    if w != w_next:
        max_ans = max(max_ans, f_x)
print(max_ans)