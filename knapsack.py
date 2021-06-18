#-*- coding: utf-8 -*-

def my_knapsack(item, m):
    #品物の数
    n = len(item)
    #DP表
    c = [[0] * (m + 1) for i in range(0, n + 1)]

    #DP表の作成
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if item[i - 1][1] <= j:
                c[i][j] = max(c[i - 1][j - item[i - 1][1]] + item[i - 1][0], c[i - 1][j])
            else:
                c[i][j] = c[i - 1][j]

    #DP表から選んだ品物を探索
    selected = [] #解に含まれる品物リスト
    j = m
    for i in range(n, 0, -1):
        if j <= 0:
            break
        elif c[i - 1][j] == c[i][j]:
            continue
        else:
            selected.append(item[i - 1])
            j = j - item[i - 1][1]
    return selected

if __name__ == "__main__":
    #品物リスト
    item = [(2, 3), (3, 3), (6, 5), (1, 3), (5, 4), (10, 7), (2, 1), (13, 12), (1, 1), (8, 11)]
    print("LIST : " + str(item))

    #最適解を探索
    m = 30 #重量の上限
    selected = my_knapsack(item, m)

    #最適解の表示
    print("OPTIMIZE : " + str(selected))
