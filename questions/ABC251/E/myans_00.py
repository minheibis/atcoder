import queue

# 1回目は特殊
# 円になっている中で最小値を求める。
# そこを切れ目にして一列の区間を構成する。

# 2回目以降は分割された区間ごとに、最小値を求めて、それで再度分割する
# それを繰り返して、１以上の区間が消滅するまで繰り返す

n = int(input())
p_list = [i for i in range(n)]
a_list = list(map(int, input().split()))
ans = 0

# 2回目以降の場合の区間について、その判定を行うかつ分割した結果を返す関数
def hantei(ans, p_a_tup):
    p_list, a_list = p_a_tup

    min_1 = min(a_list)
    ans += min_1
    min_index = a_list.index(min_1)
    p_0_index = min_index - 1
    p_1_index = min_index + 1

    if min_index == 0:
        print("is_min")
        a_list_0 = a_list[0:min_index]
        a_list_1 = a_list[min_index+1:]
        p_list_0 = []
        p_list_1 = p_list[p_1_index:]
    elif min_index == (len(a_list) - 1):
        print("is_max")
        a_list_0 = a_list[0:-1]
        a_list_1 = []
        p_list_0 = p_list[0:p_0_index]
        p_list_1 = []
    else:
        a_list_0 = a_list[0:min_index]
        a_list_1 = a_list[min_index+1:]
        p_list_0 = p_list[0:p_0_index]
        p_list_1 = p_list[p_1_index:]
        print("check_0: ", len(a_list_0) > len(p_list_0))
        print("check_1: ", len(a_list_1) > len(p_list_1))

    p_a_tup_0 = (p_list_0, a_list_0)
    p_a_tup_1 = (p_list_1, a_list_1)
    return ans, p_a_tup_0, p_a_tup_1

# 1回目
min_1 = min(a_list)
ans += min_1
min_index = a_list.index(min_1)

print("min_index: ", min_index)
if min_index == 0:
    a_list = a_list[1:]
    p_list = p_list[2:]
elif min_index == (len(a_list) - 1):
    a_list = a_list[1:]
    p_list = p_list[1:-1]
else:
    a_list_0 = a_list[0:min_index]
    a_list_1 = a_list[min_index+1:]
    p_list_0 = p_list[0:min_index]
    p_list_1 = p_list[min_index+2:]
    a_list = a_list_1 + a_list_0
    p_list = p_list_1 + p_list_0

p_a_tup = (p_list, a_list)
print("p_a_tup first: ", p_a_tup)
print("ans:", ans)

# 2回目以降
# queで実装する
q = queue.Queue()
q.put(p_a_tup)
while not q.empty():
    p_a_tup = q.get()
    print("p_a_tup: ", p_a_tup)
    ans, p_a_tup_0, p_a_tup_1 = hantei(ans, p_a_tup)
    print("ans:", ans)
    if p_a_tup_0[0] != []:
        q.put(p_a_tup_0)
    if p_a_tup_1[0] != []:
        q.put(p_a_tup_1)

print(ans)