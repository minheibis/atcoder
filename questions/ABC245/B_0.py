N = int(input())
list_a = list(map(int, input().split()))

list_a = sorted(list_a)

max_i = len(list_a) - 1
for i, a in enumerate(list_a):
    if i == 0:
        if a != 0:
            # 最初の場合も0でなければ0を返す
            print(0)
            break
    if i == max_i:
        # 最後の場合は例外, 
        print(a + 1)
        break
    elif list_a[i + 1] - a < 2:
        # 同じまたは連続の場合はOK
        continue
    else:
        print(a + 1)
        break