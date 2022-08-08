from math import sqrt

x, y = map(int, input().split())

v_len = sqrt(x**2 + y**2)

print(x/v_len, y/v_len)