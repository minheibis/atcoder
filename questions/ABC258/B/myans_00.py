import numpy as np

N = int(input())

a_map_list = []
for _ in range(N):
    a_map_list.append(list(str(input())))
a_map = np.array(a_map_list)

# 1
max_ans = int("1" * N)

def find_max_from_row(tmp_row, N, max_ans):
    for _ in range(N):
        tmp_row = np.roll(tmp_row, 1)
        max_ans = max(max_ans, int("".join(tmp_row)))
    tmp_row = np.flip(tmp_row)
    for _ in range(N):
        tmp_row = np.roll(tmp_row, 1)
        max_ans = max(max_ans, int("".join(tmp_row)))
    return max_ans

# tateyoko
for i in range(N):
    tmp_row = a_map[i]
    max_ans = find_max_from_row(tmp_row, N, max_ans)
    tmp_col = a_map[:, i]
    max_ans = find_max_from_row(tmp_col, N, max_ans)

# naname
for i in range(N):
    a_map_tmp = np.roll(a_map, i, axis=1)
    # print("a_map_tmp: \n", a_map_tmp)
    tmp_diag = np.diag(a_map_tmp)
    # print("tmp_diag: ", tmp_diag)
    max_ans = find_max_from_row(tmp_diag, N, max_ans)
a_map = np.fliplr(a_map)
for i in range(N):
    a_map_tmp = np.roll(a_map, i, axis=1)
    tmp_diag = np.diag(a_map_tmp)
    # print(tmp_diag)
    max_ans = find_max_from_row(tmp_diag, N, max_ans)

print(max_ans)