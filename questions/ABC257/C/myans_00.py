from collections import OrderedDict

N = int(input())
S_list = list(map(int, list(str(input()))))
W_list = list(map(int, input().split()))

p_dict = dict()
for w, s in zip(W_list, S_list):
    p_dict[w] = s
# print(p_dict)
p_dict = OrderedDict(sorted(p_dict.items()))
print(p_dict)

f_x = sum(S_list)
# print("f_x:", f_x)
max_ans = f_x
# p_dict.keys[0]
for w, s in p_dict.items():
    if s == 1:
        f_x -= 1
    else:
        f_x += 1
    print("f_x:", f_x)
#    if 
#        max_ans = max(max_ans, f_x)

print(max_ans)