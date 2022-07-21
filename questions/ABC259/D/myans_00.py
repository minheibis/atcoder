def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# 調査が必要なのは、整数のなので、それぞれ４つの点のみ
# dfsの感覚でよさそう？
# ではないな、中心を結んだ長さと半径の関係性で移動できるかが決まってくるのか

# 連結している円を特定
# startからのdfs

n = nextInt()
sx, sy, tx, ty = nextInts()
c_list = []
for i in range(n):
    x, y, r = nextInts()
    if x + r == sx and y == sy:
        start = i
    elif x - r == sx and y == sy:
        start = i
    elif x == sx and y + r == sy:
        start = i
    elif x == sx and y - r == sy:
        start = i
    if x + r == tx and y == ty:
        goal = i
    elif x - r == tx and y == ty:
        goal = i
    elif x == tx and y + r == ty:
        goal = i
    elif x == tx and y - r == ty:
        goal = i
    c_list.append([x, y, r])

# print(c_list)
# print(start, goal)

# 隣接行列を考える
rin_t = [[0 for _ in range(n)] for _ in range(n)]
for i, c1 in enumerate(c_list):
    for j, c2 in enumerate(c_list):
        bet2 = (c1[0] - c2[0])**2 + (c1[1] - c2[1])**2
        r2 = (c1[2] + c2[2])**2
        r2min = (c1[2] - c2[2])**2
        # print("i, j, bet2, r2:", i, j, bet2, r2)
        if r2min <= bet2 and r2 >= bet2 and i != j:
            rin_t[i][j] = 1

# print(rin_t)

seen = [0 for _ in range(n)]
def dfs(rin_t, u):
    seen[u] = 1
    for v, cango in enumerate(rin_t[u]):
        if cango == 1:
            if seen[v] == 0:
                dfs(rin_t, v)

dfs(rin_t, start)
# print("seen:", seen)
if seen[goal] == 1:
    print("Yes")
else:
    print("No")

"""
// 深さ優先探索
vector<bool> seen;
void dfs(const Graph &G, int v) {
    seen[v] = true; // v を訪問済にする

    // v から行ける各頂点 next_v について
    for (auto next_v : G[v]) { 
        if (seen[next_v]) continue; // next_v が探索済だったらスルー
        dfs(G, next_v); // 再帰的に探索
    }
}
"""