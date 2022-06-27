import math
a, b, c = map(int, input().split())
r = math.gcd(math.gcd(a,b), c)
print((a // r - 1) + (b // r - 1) + (c // r - 1))