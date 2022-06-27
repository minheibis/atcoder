def set_swap_move_list(a, n, k):
    swap_move_list = []
    for i in range(n - k):
        swap_move_list.append((i, i + k))
    return swap_move_list

#a,bの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def ans_check(n, k):
    if k < n / 2 and gcd(n, k) == 1:
        return True
    else:
        return False

def solution():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))
    sorted_a = tuple(sorted(a))
    if a == sorted_a:
        print("Yes")
        return
    if ans_check(n, k):
        # print("Yes by ans check")
        print("Yes")
        return
    swap_move_list = set_swap_move_list(a, n, k)
    new_flag = True
    pattern_set = set()
    pattern_set.add(a)
    tested_set = set()

    # print("swap_move_list", swap_move_list)
    while pattern_set:
        # print("pattern_set", pattern_set)
        pattern_now = pattern_set.pop()
        # print("pattern_now", pattern_now)
        # print("tested_set", tested_set)
        new_flag = False
        for swap_move in swap_move_list:
            a_new = list(pattern_now)
            a_new[swap_move[0]], a_new[swap_move[1]] = a_new[swap_move[1]], a_new[swap_move[0]]
            a_new = tuple(a_new)
            # print("a_new", a_new)
            if a_new not in tested_set:
                new_flag = True
                # print("sorted_a", sorted_a)
                if a_new == sorted_a:
                    print("Yes")
                    return
                else:
                    pattern_set.add(a_new)
                    tested_set.add(pattern_now)
    print("No")

solution()