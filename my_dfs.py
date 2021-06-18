# -*- coding: utf-8 -*-

#状態の種類を定義
WHITE = 0
GRAY = 1
BLACK = 2

#無限大の定義
INFTY = 2**31 - 1

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()
        self.color = WHITE
        self.dscv = INFTY
        self.cmpl = INFTY
        self.pred = None

    #頂点の情報を開示
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.color) + ", " + str(self.dscv) + ", " + str(self.cmpl) + ", " + str_pred

#幅優先探索のサブ関数
def dfs(vertices, u, time):
    u.dscv = time
    time += 1
    u.color = GRAY
    for i in u.adj:
        v = vertices[i]
        if v.color == WHITE:
            v.pred = u.id
            dfs(vertices, v, time)
            time = v.cmpl + 1
    u.color = BLACK
    u.cmpl = time
    time += 1

#経路を表示
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id)
    elif v.pred == None:
        print("\n経路が存在しません。")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id)

#頂点を接続
def connect(vertices, i, j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

if __name__ == "__main__":
    #頂点の数
    N = 8

    #頂点の生成
    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))

    #辺の設定
    connect(vertices, 0, 1)
    connect(vertices, 0, 7)
    connect(vertices, 1, 6)
    connect(vertices, 1, 2)
    connect(vertices, 2, 3)
    connect(vertices, 2, 5)
    connect(vertices, 3, 4)
    connect(vertices, 3, 5)
    connect(vertices, 4, 5)
    connect(vertices, 5, 6)

    #頂点３を始点として探索
    dfs(vertices, vertices[3], 0)

    #頂点３から頂点7の経路を表示
    print("頂点３から頂点7の経路：")
    print_path(vertices, vertices[3], vertices[7])
    print("")

    #各頂点の表示
    for i in range(0, N):
        print(vertices[i].to_string())
