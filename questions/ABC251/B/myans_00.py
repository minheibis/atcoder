import itertools

n, w = map(int, input().split())
a = list(map(int, input().split()))
len_a = len(a)

a_pairs = []
for i in range(1, 4):
    a_pairs += list(itertools.combinations(a, i))
    # 単に b_pairs += itertools.combinations(b, i) でも可

ans_set = set()
for a_pair in a_pairs:
    sum_a = sum(a_pair)
    if sum_a <= w:
        ans_set.add(sum_a)

print(len(ans_set))