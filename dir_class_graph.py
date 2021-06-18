# -*- coding: utf-8 -*-

#頂点
class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()

    def to_string(self):
        return str(self.id) + ", adj = " + str(self.adj)

#頂点を接続する辺の作成
def connect(vertices, i, j):
    vertices[i].adj.add(j)

if __name__ == "__main__":
    N = 5

    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))

    connect(vertices, 0, 1)
    connect(vertices, 0, 4)
    connect(vertices, 1, 2)
    connect(vertices, 1, 3)
    connect(vertices, 1, 4)
    connect(vertices, 2, 3)
    connect(vertices, 3, 4)

    for i in range(0, N):
        print(vertices[i].to_string())
