#-*- coding: utf-8 -*-

import heapq

#無限大の定義
INFTY = 2**31 - 1

class MyVertex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.adj = {} #dict型
        self.g = INFTY
        self.f = INFTY
        self.pred = None

    # = の定義
    def __eq__(self, v):
        return self.f == v.f

    # != の定義
    def __ne__(self, v):
        return self.f != v.f

    # < の定義
    def __lt__(self, v):
        return self.f < v.f

    # <= の定義
    def __le__(self, v):
        return self.f <= v.f

    # > の定義
    def __gt__(self, v):
        return self.f > v.f

    # >= の定義
    def __ge__(self, v):
        return self.f >= v.f

    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return str(self.id) + ", x = " + str(self.x) + ", y = " + str(self.y) + ", adj = " + str(self.adj) + ", f = " + str(self.f) + ", g = " + str(self.g) + ", pred = " + str_pred

#リストに頂点uのインスタンスが含まれるかどうかを確認
#MyVertexクラスで__eq__を定義したため、標準ライブラリのcountメソッドは使えないので注意
def is_contained(u, l):
    for v in l:
        if u.id == v.id:
            return True

#マンハッタン距離の計算
def get_dist(u, v):
    return abs(u.x - v.x) + abs(u.y - v.y)

#A*アルゴリズム
def aster(vertices, src, dest):
    #初期化
    src.g = 0
    src.f = get_dist(src, dest)
    open_list = []
    closed_list = []

    #探索開始
    open_list.append(src)
    while len(open_list) > 0:
        u = heapq.heappop(open_list)
        #頂点uが終点と同じである場合
        if u.id == dest.id:
            break;

        #隣接頂点を走査
        for i in u.adj.keys():
            v = vertices[i]
            #頂点vを経由した場合のsrcからdestへのfを計算
            f = u.g + u.adj[v.id] + get_dist(v, dest)

            if is_contained(v, open_list):
                #頂点vが未探索リストに含まれている場合
                if f < v.f:
                    v.f = f
                    v.g = u.g + u.adj[v.id]
                    v.pred = u.id
                    heapq.heapify(open_list)
            elif is_contained(v, closed_list):
                #頂点vが探索済みリストに含まれている場合
                if f < v.f:
                    v.f = f
                    v.g = u.g + u.adj[v.id]
                    v.pred = u.id
                    closed_list.remove(v)
                    open_list.append(v)
                    heapq.heapify(open_list)
            else:
                #頂点vがいずれのリストにも含まれていない場合
                v.f = f
                v.g = u.g + u.adj[v.id]
                v.pred = u.id
                open_list.append(v)
                heapq.heapify(open_list)

        #探索中の頂点を探索済みリストに追加
        closed_list.append(u)

#経路を表示
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id)
    elif v.pred == None:
        print("\n経路が存在しません。 No root in map.")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id)

#マップからグラフを生成
def to_graph(map, xmax, ymax):
    #頂点のリスト
    vertices = []

    #頂点の生成
    id = 0
    for i in range(0, ymax):
        for j in range(0, xmax):
            vertices.append(MyVertex(id, j, i))
            id += 1

    #辺の生成
    for v in vertices:
        #map[v.y][v.x]が1の場合だけ他の頂点と接続
        if map[v.y][v.x] == 1:
            #下と接続
            if v.y + 1 < ymax and map[v.y + 1][v.x] == 1:
                v.adj[(v.y + 1) * ymax + v.x] = 1
            #上と接続
            if v.y - 1 >= 0 and map[v.y - 1][v.x] == 1:
                v.adj[(v.y - 1) * ymax + v.x] = 1
            #右と接続
            if v.x + 1 < xmax and map[v.y][v.x + 1] == 1:
                v.adj[v.y * ymax + v.x + 1] = 1
            #左と接続
            if v.x - 1 >= 0 and map[v.y][v.x - 1] == 1:
                v.adj[v.y * ymax + v.x - 1] = 1

    #生成したリストを返す
    return vertices

if __name__ == "__main__":
    #マップを生成
    map = [[1,1,1,0,1,1,1,1],\
            [1,0,1,1,1,0,1,1],\
            [1,1,0,0,0,1,0,1],\
            [1,1,1,1,0,0,1,1],\
            [1,0,1,1,1,1,0,1],\
            [1,1,1,0,0,0,1,1],\
            [1,1,1,1,0,1,0,1],\
            [1,1,1,1,0,1,1,1]]
    #頂点の生成
    vertices = to_graph(map, 8, 8)

    #頂点34を始点として探索
    src = vertices[59]
    dest = vertices[53]
    aster(vertices, src, dest)

    #頂点34から頂点54の経路を表示
    print("頂点34から頂点54の経路：")
    print_path(vertices, src, dest)
    print("")
