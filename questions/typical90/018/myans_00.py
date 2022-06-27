from math import sin, cos, pi, acos, degrees, sqrt

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())
    x = X
    y = (Y + L/2 * sin(E/T * 2 * pi))
    z = (L/2 - L/2 * cos(E/T * 2 * pi))
    xy = x ** 2 + y ** 2
    xyz = xy + z ** 2
    print(degrees(acos(sqrt(xy/xyz))))