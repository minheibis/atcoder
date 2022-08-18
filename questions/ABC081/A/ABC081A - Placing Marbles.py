a = int(input())

def count_ones_by_bitmask(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

ans = count_ones_by_bitmask(a & 0b111)
print(ans)