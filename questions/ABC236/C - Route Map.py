N, M = map(int, input().split())
S_list = list(map(str, input().split()))
T_list = list(map(str, input().split()))

#print(N, M)
#print(S_list)
#print(T_list)

ans_list = ["No"] * N

s_pos = 0
for i, t in enumerate(T_list):
    while 1:
        if t == S_list[s_pos]:
            ans_list[s_pos] = "Yes"
            s_pos += 1
            break
        s_pos += 1

print(*ans_list, sep="\n")