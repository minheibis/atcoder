N = int(input())
A = list(map(int, input().split()))
A_set = set(A)
A_set_max = max(A_set)

A_no_dup_list = sorted(set(A), key=A.index)
[1, 5, 4, 7, 2, 8, 3]

B = [i for i in A if i != A_set_max]

#print("N", N)
print("A", A)
print("A_set", A_set)
print(*B)
