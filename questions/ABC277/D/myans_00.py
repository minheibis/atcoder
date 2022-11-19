def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, M = nextInts()
A_list = nextIntList()

A_list.sort()

old_a = A_list[0]
count_max = old_a
count_max_now = old_a

if old_a == 0:
    from_0_flag = True
    from_0_count = old_a
else:
    from_0_flag = False
    from_0_count = 0

# print(A_list)
for a in A_list[1:]:
    # print("a: ", a)
    # print("count_max_now: ", count_max_now)
    if a - old_a > 1:
        count_max = max(count_max, count_max_now)
        # print("count_max: ", count_max)
        if from_0_flag:
            from_0_count = count_max_now
            from_0_flag = False
        count_max_now = a
    else:
        count_max_now += a
    old_a = a

count_max = max(count_max, count_max_now)
# print("count_max: ", count_max)
if A_list[-1] == M - 1:
    # print("is ring")
    # print("from_0_count: ", from_0_count)
    # print("count_max_now: ", count_max_now)
    count_long = from_0_count + count_max_now
    count_long = min(sum(A_list), count_long)
    count_max = max(count_long, count_max)
    # print("count_max: ", count_max)

print(sum(A_list) - count_max)