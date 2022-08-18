import sys
import math

N = int(input())

T_list = []
for l in sys.stdin:
    t_dict = {}
    t_dict["x"], t_dict["y"] = map(int, l.split())
    T_list.append(t_dict)

max_len = 0

for t_dict_0 in T_list:
    for t_dict_1 in T_list:
        t_len = math.sqrt(
            (t_dict_0["x"] - t_dict_1["x"])**2 + 
            (t_dict_0["y"] - t_dict_1["y"])**2
        )
        max_len = max(max_len, t_len)

print(max_len)