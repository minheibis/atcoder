import sys

N = int(input())

T_list = []
for l in sys.stdin:
    t_dict = {}
    t_dict["t"], t_dict["x"], t_dict["y"] = map(int, input().split())
    T_list.append(t_dict)

def can_walk(t, x, y, old_t, old_x, old_y):
    diff_t = t - old_t
    diff_x = abs(x - old_x)
    diff_y = abs(y - old_y)
    diff_x_y = diff_x + diff_y
    if diff_x_y > diff_t:
        return False
    if diff_t % 2 != diff_x_y % 2:
        return False
    return True

def calc(N, T_list):
    old_t, old_x, old_y = 0, 0, 0

    for i in range(N):
        t_dict = T_list[i]
        if can_walk(t_dict["t"], t_dict["x"], t_dict["y"], old_t, old_x, old_y):
            old_t, old_x, old_y = t_dict["t"], t_dict["x"], t_dict["y"]
        else:
            print("No")
            return
    
    print("Yes")
    return

calc(N, T_list)