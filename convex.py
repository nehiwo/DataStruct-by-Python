#-*- coding: utf-8 -*-

import math

def get_vector(point1, point2):
    return (point2[0] - point1[0], point2[1] - point1[1])

def get_norm(vector):
    return math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])

def cross_prod(vector1, vector2):
    return vector1[0] * vector2[1] - vector1[1] * vector2[0]

def get_start_point(points):
    min_y = 2**31 - 1
    for point in points:
        if point[1] <= min_y:
            min_y = point[1]

    min_x = 2**31 - 1
    min_point = None
    for point in points:
        if point[1] == min_y and point[0] < min_x:
            min_x = point[0]
            min_point = point
    return min_point

#ギフト包装法
def gift_wrapping(points):
    #凸包に含まれる点のリスト
    ch = []

    #スタート地点決定（座標平面上１番左下の点）
    start_point = get_start_point(points)
    edge_point = start_point

    #探索開始
    while True:
        ch.append(edge_point)
        next_point = points[0]
        for i in range(1, len(points)):
            target_point = points[i]
            if next_point == edge_point:
                next_point = target_point
            else:
                #外積が正なら点はベクトルの左側、負なら右側、0なら直線上に位置する
                vector1 = get_vector(edge_point, next_point)
                vector2 = get_vector(edge_point, target_point)
                prod = cross_prod(vector1, vector2)
                if prod > 0:
                    next_point = target_point
                elif prod == 0 and get_norm(vector2) > get_norm(vector1):
                    next_point = target_point
                else:
                    continue

        #走査中の点を移動
        edge_point = next_point

        #走査の終了
        if edge_point == start_point:
            break

    return ch

if __name__ == "__main__":
    points = [(1, 1), (3, 1), (2, 3), (6, 4), (4, 3), (4, 6), (1, 5), (4, 5)]
    print("Set of Points : " + str(points))

    ch = gift_wrapping(points)

    print("Convex Hull : " + str(ch))
