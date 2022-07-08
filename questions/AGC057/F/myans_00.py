def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())


def euclid(a, b):
    # make b larger than a
    if a > b:
        a, b = b, a
    count_a_list = []
    while a:
        count_a_list.append(b // a)
        a, b = b % a, a
    return count_a_list

def solve():
    case = sorted(nextIntList())
    if len(set(case)) == 1:
        return 1
    elif len(set(case)) == 2:
        return 2
    count_a_list = euclid(case[2] - case[1], case[1] - case[0])
    if len(count_a_list) == 1 and count_a_list[0] == 1:
        return 5 # this exception is needed too
    count_a_list[-1] -= 1
    ans, num, prv = 1, 1, 1
    for count_a in count_a_list:
        ans += (num - prv + 1) * count_a * (count_a + 1) + (prv - 1) * count_a * 2
        tmp = num
        num = (num - prv + 1) * (count_a + 1) + prv - 1
        prv = tmp - prv + 1
        ans %= MOD
        prv %= MOD
        num %= MOD
    
    ans = (ans - (num - prv * 2) + (num + 1) * 2) % MOD
    return ans 

MOD = 998244353

def main():
    t = nextInt()
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()
