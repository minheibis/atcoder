#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V): 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納

#この関数がワーシャルフロイド法。
#移動コスト一覧表dと、頂点の数nがあれば動作する。

#iとjが始点と終点で、それをすべてのkを通る形ですべての始点と終点を全検索しているのですべての経路を検証網羅している。
#この時、k（中継点）を使わないなら d[i][j] そのまま、k を使うとd[i][k] + d[k][j] が最短となる。