def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, A, B = nextInts()
S = str(input())

ans = N * max(A, B)
for i in range(N):
    count_B = 0
    for j in range(N // 2):
        if S[(j + i) % N] != S[(N-1-j + i) % N]:
            count_B += 1
    tmp_ans = i * A + count_B * B
    ans = min(ans, tmp_ans)

print(ans)