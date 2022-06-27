num_list = list(map(int, input().split()))

ans = 0
for _ in range(3):
    ans = num_list[ans]
print(ans)