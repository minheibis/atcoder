from copy import deepcopy

class B_i:
    def __init__(self):
        # 最後の集合のリスト
        self.last_list = []
        self.last_list_min = 0
        self.last_list_max = 0
        self.last_min_max_diff = 0
        # 最後を除いた積
        self.product_no_last = 1
        self.product_all = 0
        self.one_flag = False
    
    def print_B_i(self):
        print("last_list", self.last_list)
        print("last_list_min", self.last_list_min)
        print("last_list_max", self.last_list_max)
        print("last_min_max_diff", self.last_min_max_diff)
        print("one_flag", self.one_flag)
        print("product_no_last", self.product_no_last)
        print("product_all", self.product_all)

    def set_new_last(self, value):
        self.last_list = [last_value]
        self.last_list_min = last_value
        self.last_list_max = last_value
        self.last_min_max_diff = 0

    def append_last_set(self, value):
        self.last_list.append(value)
        flag = False
        if self.last_list_min > value:
            self.last_list_min = value
            flag = True
        if self.last_list_max < value:
            self.last_list_max = value
            flag = True
        if flag:
            self.last_min_max_diff = self.last_list_max - self.last_list_min

    def calc_product(self):
        self.product_all = (self.product_no_last * self.last_min_max_diff)

N = int(input())
A_list = list(map(int, input().split()))
len_A_list = len(A_list)
# 空のdp_listを作成
dp_list = [0 for _ in range(len_A_list)]

dp_0 = B_i()
last_value = A_list[0]
dp_0.set_new_last(last_value)
dp_0.one_flag = True

#print("dp_0")
#dp_0.print_B_i()

dp_list[0] = [dp_0]

for i in range(1, len_A_list):
    # ここで追加する値
    last_value = A_list[i]

    b_i_list = []
    for b_i_1 in dp_list[i - 1]:
        # 2つに分かれる
        # 独立してつける場合
        if b_i_1.one_flag == False:
            # 最後の1つ前が0
            b_i_first = deepcopy(b_i_1)

            b_i_first.set_new_last(last_value)   
            # それまでのproduct_allを1つ前までの積として保存する
            b_i_first.product_no_last = b_i_first.product_all
            b_i_first.product_all = 0
            b_i_second.one_flag = True

            #print("b_i_first", i, last_value)
            #b_i_first.print_B_i()
            b_i_list.append(b_i_first)

        # 最後のセットに追加する場合
        b_i_second = deepcopy(b_i_1)
        b_i_second.append_last_set(last_value)
        # product_no_lastは更新せず、product_allを更新する。
        b_i_second.calc_product()
        b_i_second.one_flag = False

        #print("b_i_second", i, last_value)
        #b_i_second.print_B_i()
        b_i_list.append(b_i_second)
    dp_list[i] = b_i_list

# 結果の表示
print(sum([b_i.product_all for b_i in dp_list[len_A_list - 1]]) % 998244353)
