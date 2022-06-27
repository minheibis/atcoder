import sys

N = int(input())

d_list = []
for l in sys.stdin:
    d_list.append(int(l))

print(len(set(d_list)))