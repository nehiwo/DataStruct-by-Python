# -*- coding: utf-8 -*-

#頂点を接続する辺の作成
def connect(graph, i, j):
    graph[i][j] = 1
    graph[j][i] = 1

#グラフ情報の表示
def pretty_print(graph, n):
    print("   ")
    for i in range(0, n):
        print(str(i) + " ")

    for i in range(0, n):
        print(str(i) + " ")
        for j in range(0, n):
            print(str(graph[i][j]) + " ")
        print("")

if __name__ == "__main__":
    N = 5

    graph = [[0 for i in range(0, N)] for j in range(0, N)]

    connect(graph, 0, 1)
    connect(graph, 0, 4)
    connect(graph, 1, 2)
    connect(graph, 1, 3)
    connect(graph, 1, 4)
    connect(graph, 2, 3)
    connect(graph, 3, 4)

    pretty_print(graph, N)
