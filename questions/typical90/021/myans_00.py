def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
to_list = [set() for _ in range(N)]
from_list = [set() for _ in range(N)]
for _ in range(M):
    a, b = nextInts()
    a -= 1
    b -= 1
    # print("a, b: ", a, b)
    to_list[a].add(b) # a から b にいける
    from_list[b].add(a) # b に a からいける
    for can_go_to_a in from_list[a]: # a にもともと行けた can_go_to_a について
        to_list[can_go_to_a].add(b) # can_go_to_a から b に行けるようになる。
        from_list[b].add(can_go_to_a) # b に can_go_to_a からいけるようになる。
    for can_go_from_b in to_list[b]: # b からもともと行けた can_go_from_b について
        to_list[a].add(can_go_from_b) # a から can_go_from_b にいけるようになる
        from_list[can_go_from_b].add(a) # can_go_from_b に a から行けるようになる。

    # print("to_list: ", to_list)
    # print("from_list: ", from_list)
# print("to_list: ", to_list)
# print("from_list: ", from_list)

ans_set = set()
for p, (to_set, from_set) in enumerate(zip(to_list, from_list)):
    have_path_set = to_set & from_set
    for have_path_p in have_path_set:
        if not p == have_path_p:
            if p > have_path_p:
                ans_set.add((have_path_p, p))
            else:
                ans_set.add((p, have_path_p))
# print("ans_set", ans_set)
print(len(ans_set))