from collections import deque
import copy

N = int(input())
C_list = [(c, i + 1) for i, c in enumerate(list(map(int, input().split())))]
C_list.sort()
C_deq = deque(C_list)

#print("N", N)
#print("C_list", C_list)

ans = 0
comp_set = set()

i = 0
while len(C_deq) > 0:
    c, num = C_deq.popleft()
    if num not in comp_set:
        ans += c
        comp_set_tmp = copy.copy(comp_set)
        for num_in in comp_set_tmp:
            comp_set.add(num_in ^ num)
        comp_set.add(num)

print(ans)