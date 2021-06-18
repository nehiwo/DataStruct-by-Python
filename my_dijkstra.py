#-*- coding: utf-8 -*-

import heapq

#無限大の定義
INFTY = 2**31 - 1

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = {} #dict型
        self.dist = INFTY
        self.pred = None

    # = の定義
    def __eq__(self, v):
        return self.dist == v.dist

    # != の定義
    def __ne__(self, v):
        return self.dist != v.dist

    # < の定義
    def __lt__(self, v):
        return self.dist < v.dist

    # <= の定義
    def __le__(self, v):
        return self.dist <= v.dist

    # > の定義
    def __gt__(self, v):
        return self.dist > v.dist

    # >= の定義
    def __ge__(self, v):
        return self.dist >= v.dist

    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.dist) + ", " + str_pred

#最短経路となる先行頂点の変更
def relax(u, v):
    if v.dist > u.dist + u.adj[v.id]:
        v.dist = u.dist + u.adj[v.id]
        v.pred = u.id
        return True
    else:
        return False

#ダイクストラ法
def dijkstra(vertices, src):
    #初期化
    src.dist = 0
    q = [] #優先度付きキュー
    for u in vertices:
        heapq.heappush(q, u)

    #探索開始
    while len(q) > 0:
        print_heap(q) #ヒープの中身表示
        u = heapq.heappop(q)
        for i in u.adj.keys():
            if relax(u, vertices[i]):
                heapq.heapify(q)

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
def connect(vertices, i, j, weight):
    vertices[i].adj[j] = weight

#ヒープの中身表示
def print_heap(q):
    str_heap = "[ "
    for i in q:
        str_heap += str(i.id) + " "
    print(str_heap + "]")

if __name__ == "__main__":
    #頂点の数
    N = 5

    #頂点の生成
    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))

    #辺の設定
    connect(vertices, 0, 1, 15)
    connect(vertices, 0, 4, 7)
    connect(vertices, 1, 2, 1)
    connect(vertices, 1, 4, 3)
    connect(vertices, 2, 3, 5)
    connect(vertices, 3, 2, 6)
    connect(vertices, 3, 0, 9)
    connect(vertices, 4, 1, 4)
    connect(vertices, 4, 2, 11)
    connect(vertices, 4, 3, 2)

    #頂点0を始点として探索
    dijkstra(vertices, vertices[0])

    #頂点0から頂点2の経路を表示
    print("頂点0から頂点2の経路：")
    print_path(vertices, vertices[0], vertices[2])
    print("")

    #各頂点の表示
    for i in range(0, N):
        print(vertices[i].to_string())
