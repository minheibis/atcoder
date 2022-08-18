def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

n = nextInt()
a_list = nextIntList()

same = 0
ans = 0
for i, a in enumerate(a_list):
    a -= 1
    # print("i, a", i, a)
    if i == a:
        # print("same i, a", i, a)
        same += 1
    elif i != a:
        if a_list[a] == (i + 1):
            # print("diff i, a", i, a)
            ans += 1

if same > 1:
    ans += int(same * (same-1))

print(ans // 2)