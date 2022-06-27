import copy

class Modint:
    mod = 0
#    has_been_set = False

    def __init__(self, v = 0, m = None):
        if m != None:
#            assert m >= 1
#            assert not Modint.has_been_set
            Modint.mod = m # クラス変数
#            Modint.has_been_set = True
#        assert Modint.has_been_set
        if 0 <= v < Modint.mod:
            self._v = v
        else:
            self._v = v % Modint.mod
    
    def __add__(self, other):
        if isinstance(other, Modint):
            res = self._v + other._v
            if res > Modint.mod:
                res -= Modint.mod
        else:
            res = self._v + other
        return Modint(res)
    
    def __sub__(self, other):
        if isinstance(other, Modint):
            res = self._v - other._v
            if res < 0:
                res += Modint.mod
        else:
            res = self._v - other
        return Modint(res)
    
    def __mul__(self, other):
        if isinstance(other, Modint):
            return Modint(self._v * other_v)
        else:
            return Modint(self._v * other)

    def __floordiv__(self, other):
        if isinstance(other, Modint):
            other = other._v
        inv = pow(other, Modint.mod-2, Modint.mod) #逆元を求める
        return Modint(self._v * inv)

    def __pow__(self, other):
        assert isinstance(other, int) and other >= 0
        return Modint(pow(self._v, other, Modint.mod))

    def __iadd__(self, other):
        if isinstance(other, Modint):
            self._v += other._v
            if self._v >= Modint.mod:
                self._v -= Modint.mod
        else:
            self._v += other
            if self._v < 0 or self._v >= Modint.mod:
                self._v %= Modint.mod
        return self
    
    def __isub__(self, other):
        if isinstance(other, Modint):
            self._v -= other._v
            if self._v < 0:
                self._v += Modint.mod
        else:
            self._v -= other
            if self._v < 0 or self._v >= Modint.mod:
                self._v %= Modint.mod
        return self

    def __imul__(self, other):
        if isinstance(other, Modint):
            self._v *= other._v
        else:
            self._v *= other
        if self._v < 0 or self._v >= Modint.mod:
            self._v %= Modint.mod
        return self
    
    def __ifloordiv__(self, other):
        if isinstance(other, Modint):
            other = other._v
        inv = pow(other, Modint.mod-2, Modint.mod)
        self._v *= inv
        if self.v > Modint.mod:
            self._v %= Modint.mod
        return self

    def __ipow__(self, other):
        assert isinstance(other, int) and other >= 0
        self._v = pow(self._v, other, Modint.mod)
        return self

    def __radd__(self, other):
        return Modint(other + self._v)
    
    def __rsub__(self, other):
        return Modint(other - self._v)
    
    def __rmul__(self,other):
        return Modint(other * self._v)
    
    def __rfloordiv__(self, other):
        inv = pow(self._v, Modint.mod - 2, Modint.mod)
        return Modint(other * inv)

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

    def __str__(self):
        return str(self._v) #表示用の関数

    def __repr__(self):
        return str(self._v)
    
    def __int__(self):
        return self._v

def sum_list(count_list):
    ans = 0
    for count_one in count_list:
        ans += count_one
    return ans

mod = 998244353
Modint(m = mod)

n = int(input())

count_list = [Modint(0)] + [Modint(1)] * 9
for i in range(n-1):
    new_count_list = copy.copy(count_list)
    for j, count_one in enumerate(count_list):
        if j == 0:
            new_count_list[j] = count_list[j]
        elif j == 1:
            new_count_list[j] = count_list[1] + count_list[2]
        elif j == 9:
            new_count_list[j] = count_list[8] + count_list[9]
        else:
            new_count_list[j] = count_list[j - 1] + count_list[j] + count_list[j + 1]
    # print(new_count_list)
    count_list = new_count_list
    print("i: ", i, sum_list(count_list))
    print("i_1: ", i, count_list[1])

print(sum_list(count_list))