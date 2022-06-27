# a,b,cの最大公約数を求める。
# a, bの最大公約数と、cの最大公約数を求める。

# a, b, cをそれぞれrで割って1を引いた回数がそれぞれの切断回数

# 互助法により最大公約数を求める
def gcd(a, b):
    r = a % b

    # 割り切れた場合には、割った時のbが最大公約数
    while r != 0:    
        a, b = b, r
        r = a % b
    
    return b

a, b, c = map(int, input().split())
r = gcd(gcd(a, b), c)
ans = (a + b + c) // r - 3
print(ans)