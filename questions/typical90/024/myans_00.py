# https://atcoder.jp/contests/typical90/submissions/31629442
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sub_sum = 0
for i in range(N):
  sub_sum += abs(A[i] - B[i])
    
if sub_sum <= K and (K - sub_sum) % 2 == 0:
  print("Yes")
else:
  print("No")
