N = int(input())
A = []

for i in range(2*N -1):
  a = [int(c) for c in input().split(" ")]
  A.append([-1]*i + a)

print(A)

from collections import deque

d = deque()

for i in range(1,2*N):
  d.append((A[0][i-1], [c for c in range(1 ,2*N) if not c == i]))

print("d", d)

m = 0  
while len(d) > 0:
  #print(d)
  e = d.popleft()
  print("e", e)
  if len(e[1]) == 0:
    if m < e[0]:
      m = e[0]
  else:
    eA = e[0]
    for j in range(1,len(e[1])):
      d.append((eA^A[e[1][0]][e[1][j]-1],[e[1][c] for c in range(1 ,len(e[1])) if not c == j]))
  print("d", d)

print(m)    