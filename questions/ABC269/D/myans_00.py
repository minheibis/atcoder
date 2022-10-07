def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

around_xy = [
    (-1, -1),
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
    (1, 1)
]


def solve():
    N = nextInt()
    xy_list = []
    for _ in range(N):
        x, y = nextInts()
        xy_list.append((x, y))
    groups = []
    for x, y in xy_list:
        is_in_group = False
        for group in groups:
            print("group: ", group)
            for x_tmp, y_tmp in group:
                for x_pl, y_pl in around_xy:
                    if x == (x_tmp + x_pl) and y == (y_tmp + y_pl):
                        group.append((x, y))
                        is_in_group = True
                        break
                if is_in_group == True:
                    break
        if is_in_group == False:
            groups.append([(x, y)]) 
        print("groups:", groups)
    print(len(groups))

solve()