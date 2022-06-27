from functools import lru_cache

# ある点にN回で行くルート
# = ある点の隣接する点にN-1回で行くルート
# これを帰納的に考えて、ある点に0回で行くルートまで帰納すると、ある点==最初の点であれば1回と考えられる。
# 途中でキャッシュで保存できそう
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


@lru_cache
def count_direct_root_end(p, edge_list):
    end_set = set()
    for root in edge_list:
        if root[0] == p:
            end_set.add(root[1])
        elif root[1] == p:
            end_set.add(root[0])
    return end_set

@lru_cache
def count_route(start, end, move_time, edge_list):
    print("start, end, move_time: ", start, end, move_time)
    # 終了条件
    if move_time == 0:
        if start == end:
            return Modint(1)
        else:
            return Modint(0)
    # 再帰の場合
    end_set = count_direct_root_end(end, edge_list)
    count = Modint(0)
    for next_end in end_set:
        count += count_route(start, next_end, move_time - 1, edge_list)
    return count

mod = 998244353
Modint(m = mod)

N, M, K, S, T, X = map(int, input().split())
edge_list = []
for _ in range(M):
  a, b = map(int, input().split())
  edge_list.append((a, b))

print(edge_list)
print(tuple(edge_list))
edge_list = tuple(edge_list)

count = count_route(S, T, K, edge_list)
print(count)