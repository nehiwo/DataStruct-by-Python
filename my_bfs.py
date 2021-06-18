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
        self.dist = INFTY
        self.pred = None

    #頂点の情報を開示
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.color) + ", " + str(self.dist) + ", " + str_pred

#幅優先探索
def bfs(vertices, src):
    #始点頂点の初期化
    src.color = GRAY
    src.dist = 0
    src.pred = None

    #探索
    q = [src]
    while len(q) > 0:
        u = q.pop(0)
        for i in u.adj:
            v = vertices[i]
            if v.color == WHITE:
                v.color = GRAY
                v.dist = 1
                v.pred = u.id
                q.append(v)
        u.color = BLACK

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
    bfs(vertices, vertices[3])

    #頂点３から頂点7の経路を表示
    print("頂点３から頂点7の経路：")
    print_path(vertices, vertices[3], vertices[7])
    print("")

    #各頂点の表示
    for i in range(0, N):
        print(vertices[i].to_string())
