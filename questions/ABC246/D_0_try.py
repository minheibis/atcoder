def f_d(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3

for a in range(10):
    for b in range(10):
        print(a, b ,f_d(a, b))