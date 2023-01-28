# https://note.com/kai1023/n/nf116047654aa#52b97b9e-a796-4319-b055-3d8c2d8cc07b

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

dp = [[False for _ in range(X+1)] for __ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        for k in range(b[i]+1):
            if dp[i][j] and j+a[i]*k<=X:
                dp[i+1][j+a[i]*k] = True
if dp[N][X]:
    print("Yes")
else:
    print("No")            