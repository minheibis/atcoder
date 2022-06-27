N, A, B = map(int, input().split())

sum_sum = 0
for n in range(1, N + 1):
    num_list = list(map(int, str(n)))
    num_sum = sum(num_list)
    if num_sum >= A and num_sum <= B:
        #print(n)
        sum_sum += n

print(sum_sum)