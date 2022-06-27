# pythonでの最速回答
# https://atcoder.jp/contests/typical90/submissions/29481623
import math
A, B, C = list(map(int, input().split()))
gcd1 = math.gcd(A,B)
gcd2 = math.gcd(B,C)
gcd = math.gcd(gcd1,gcd2)
print(int((A//gcd-1)+(B//gcd-1)+(C//gcd-1)))