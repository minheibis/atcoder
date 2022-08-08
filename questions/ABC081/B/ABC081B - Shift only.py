import functools
import operator

N = int(input())
A = list(map(int, input().split()))

count = 0
while functools.reduce(operator.add, [a % 2 for a in A], 0) == 0:
    #print(A)
    A = [a / 2 for a in A]
    count += 1
print(count)