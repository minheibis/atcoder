def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
A_list = nextIntList()

odd_list = list()
even_list = list()
for a in A_list:
    if a % 2 == 0:
        even_list.append(a)
    else:
        odd_list.append(a)

even_list.sort(reverse=True)
odd_list.sort(reverse=True)

ans = -1
if len(even_list) >= 2:
    ans = max(even_list[0] + even_list[1], ans)
if len(odd_list) >= 2:
    ans = max(odd_list[0] + odd_list[1], ans)
print(ans)