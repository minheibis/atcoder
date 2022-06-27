
from collections import deque
from math import floor, log2

class Modint:
    mod = 0
    has_been_set = False

    def __init__(self, v=0, m=None):
        if m != None: 
            assert m >= 1
            assert not Modint.has_been_set
            Modint.mod = m
            Modint.has_been_set = True
        assert Modint.has_been_set
        self._v = v if 0 <= v < Modint.mod else v % Modint.mod


    def __add__(self, other):
        if isinstance(other, Modint):
            res = self._v + other._v
            if res > Modint.mod: res -= Modint.mod
        else:
            res = self._v + other
        return Modint(res)

    def __sub__(self, other):
        if isinstance(other, Modint):
            res = self._v - other._v
            if res < 0: res += Modint.mod
        else:
            res = self._v - other
        return Modint(res)

    def __mul__(self, other):
        if isinstance(other, Modint):
            return Modint(self._v * other._v)
        else:
            return Modint(self._v * other)

    def __floordiv__(self, other):
        if isinstance(other, Modint): other = other._v
        inv = pow(other, -1, Modint.mod)
        return Modint(self._v * inv)

    def __pow__(self, other):
        assert isinstance(other, int) and other >= 0
        return Modint(pow(self._v, other, Modint.mod))

    def __radd__(self, other):
        return Modint(self._v + other)

    def __rsub__(self, other):
        return Modint(other - self._v)  

    def __rmul__(self, other):
        return Modint(self._v * other)

    def __rfloordiv__(self, other):
        inv = pow(self._v, -1, Modint.mod)
        return Modint(other * inv)

    def __iadd__(self, other):
        if isinstance(other, Modint):
            self._v += other._v
            if self._v >= Modint.mod: self._v -= Modint.mod
        else:
            self._v += other
            if self._v < 0 or self._v >= Modint.mod: self._v %= Modint.mod
        return self

    def __isub__(self, other):
        if isinstance(other, Modint):
            self._v -= other._v
            if self._v < 0: self._v += Modint.mod
        else:
            self._v -= other
            if self._v < 0 or self._v >= Modint.mod: self._v %= Modint.mod
        return self

    def __imul__(self, other):
        if isinstance(other, Modint):
            self._v *= other._v
        else:
            self._v *= other
        if self._v < 0 or self._v >= Modint.mod: self._v %= Modint.mod
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Modint): other = other._v
        inv = pow(other, -1, Modint.mod)
        self._v *= inv       
        if self._v > Modint.mod: self._v %= Modint.mod
        return self

    def __ipow__(self, other):
        assert isinstance(other, int) and other >= 0
        self._v = pow(self._v, other, Modint.mod)
        return self

    def __eq__(self, other):
        if isinstance(other, Modint):
            return self._v == other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v == other

    def __ne__(self, other):
        if isinstance(other, Modint):
            return self._v != other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v != other

# 追加
    def __lt__(self, other):
        if isinstance(other, Modint):
            return self._v < other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v < other

    def __gt__(self, other):
        if isinstance(other, Modint):
            return self._v > other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v > other

    def __le__(self, other):
        if isinstance(other, Modint):
            return self._v <= other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v <= other
    
    def __ge__(self, other):
        if isinstance(other, Modint):
            return self._v >= other._v
        else:
            if other < 0 or other >= Modint.mod:
                other %= Modint.mod
            return self._v >= other
    
    def __str__(self):
        return str(self._v)

    def __repr__(self):
        return str(self._v)

    def __int__(self):
        return self._v

Modint(m = 998244353)

def calclog2(a):
    #print("a", a)
    rev = 1
    #print("rev", rev)
    ans = 0
    while a > rev:
        rev<<=1
        ans += 1
        #print(rev)
        #print(ans)
    ans -= 1
    return ans

def fnc_a(X):
    if (X == 0) | (X == 1) | (X==2):
        print(X)
        return
    else:
        # logでn, mを調べる
        n = calclog2(X / 2)
        m = calclog2(X / 3)
        #print(n, m)
        len_ans_min = pow(2, n)
        if n != m:
            res_num = int(X - 2 * len_ans_min)
        else:
            res_num = int(X - 3 * len_ans_min)
        
        ans = Modint(1)
        if n != m:
            # print("is not same")
            #同数でない時、個数は維持
            num_m = res_num
            num_n = len_ans_min - num_m
        else:
            #同数の時(増加中)
            num_m = len_ans_min - res_num
            num_n = res_num*2
        # nの計算
        ans *= pow(Modint(2), num_n)
        # mの計算
        ans *= pow(Modint(3), num_m)
        #print("X, n, m, res_num, num_n, num_m, ans", X, n, m, res_num, num_n, num_m, ans)
        ans = Modint(int(ans))
        print(X, ans)

if __name__=="__main__":
    for i in range(10**18 + 1, 10**17, -1):
        fnc_a(i)