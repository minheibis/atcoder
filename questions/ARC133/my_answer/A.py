N = int(input())
A = list(map(int, input().split()))

rem_num = A[-1]
for i, (a, b) in enumerate(zip(A[:-1], A[1:])):
    if a > b:
        rem_num = a
        break

#print(A[0:i])
#print(A[i:])
ans_list = [j for j in A if j != rem_num]
#ans_list = A[0:i] + [j for j in A[i:] if j != a]

# print("A", A)
print(*ans_list)
