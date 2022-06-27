from itertools import product

A = int(input())
B = int(input())
C = int(input())
X = int(input())



count = 0
for a, b, c in product(range(A + 1), range(B + 1), range(C + 1)):
    coin_sum = a * 500 + b * 100 + c * 50
    if coin_sum == X:
        count += 1

print(count)