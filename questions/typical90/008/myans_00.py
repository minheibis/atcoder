def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

MOD = 10**9 + 7

N = int(input())
S = list(str(input()))

list_let = list("atcoder")
count_let = [0 for _ in range(N)]
for si in S:
    for i, let in enumerate(list_let):
        if si == let:
            if i == 0:
                count_let[0] += 1
                count_let[0] %= MOD
            else:
                count_let[i] += count_let[i-1]
                count_let[i] %= MOD
    # print("si, count_let: ", si, count_let)
print(count_let[len(list_let)-1])