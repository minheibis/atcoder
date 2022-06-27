_,X=map(int,input().split())
S=input()
T=[]
for c in S:
  if c=="U" and len(T)>0 and (T[-1]=="L" or T[-1]=="R"):
    T.pop()
  else:
    T.append(c)

print(T)

for c in T:
  if c=="U": X=X//2
  if c=="L": X=X*2
  if c=="R": X=X*2+1

print(X)