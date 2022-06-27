# pythonでの最速回答
# https://atcoder.jp/contests/typical90/submissions/29481623
# 26ms
import math
from sys import stdin

a, b, c = map(int, stdin.readline().split())
r = math.gcd(math.gcd(a,b), c)
print((a + b + c) // r - 3)