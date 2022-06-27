import sys
from copy import copy
from functools import lru_cache

N, M = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = list(map(int, input().split()))
list_d = list(map(int, input().split()))
c_list = tuple(zip(list_a, list_b))
b_list = tuple(zip(list_c, list_d))

@lru_cache
def isin_box(c_now, b_now):
    if (c_now[0] <= b_now[0]) and (c_now[1] <= b_now[1]):
        return True
    else:
        return False

@lru_cache
def dfs(c_list, b_list):
    if len(c_list) == 0:
        # 全てのチョコが箱に入ったのでOK
        print("Yes")
        sys.exit()
    else:
        for c_i, c_now in enumerate(c_list):
            for b_i, b_now in enumerate(b_list):
                if isin_box(c_now, b_now):
                    c_list_now = copy(list(c_list))
                    c_list_now.pop(c_i)
                    c_list_now = tuple(c_list_now)
                    b_list_now = copy(list(b_list))
                    b_list_now.pop(b_i)
                    b_list_now = tuple(b_list_now)
                    dfs(c_list_now, b_list_now)
    
dfs(c_list, b_list)
print("No")