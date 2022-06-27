
"""
Pythonでアルゴリズム（セグメント木）（実践）
https://qiita.com/takayg1/items/c811bd07c21923d7ec69
をもとに実装
"""

# 初期設定
# ここは関数オペレーターで実装する方がいいのではないか。
# https://qiita.com/mosamosa/items/d17ab5af6e19f67202cb


#####segfunc#####
def segfunc(x, y):
    return x + y
#################

#####ide_ele#####
ide_ele = 0
#################

class SegTree:
    """
    init(init_val, ide_else): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l. r): 区間(l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index i.e. 1が最小値)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length() # bit_lengthについては後で確認
        self.tree = [ide_ele] * 2 * self.num # 初期値して全てのところに単位元を代入

        # 配列の値を葉にセット（木の全体では後半の部分）
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            # 逆から構築していって、最終的に上を作るイメージ
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])


    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0 - index)
        x: update value
        """
        k += self.num # 後半の1つしか入ってないところを見たい
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1]) # 引数同士のビット単位の XOR (排他的 OR) を与えます。引数は整数でなければなりません。
            k >>= 1 
    
    # ここについては写経ではなくもう少しbit演算について理解を深めてから出直してきたい。
    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# AとBと二つのセグメント木を実装する。
# それぞれを使い分けながら答えていく。

N = int(input())
A_list = []
B_list = []
for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        A_list.append(p)
        B_list.append(0)
    else:
        A_list.append(0)
        B_list.append(p)

seg_A = SegTree(A_list, segfunc, ide_ele)
seg_B = SegTree(B_list, segfunc, ide_ele)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    print(seg_A.query(l, r), seg_B.query(l, r))
