#-*- coding: utf-8 -*-

import convex
import random
import tkinter

if __name__ == "__main__":
    points = []
    for i in range(0, 100):
        while True:
            point = (random.randint(10, 590), random.randint(10, 590))
            if points.count(point) == 0:
                points.append(point)
                break
    print("Set of Points : " + str(points))

    ch = convex.gift_wrapping(points)

    print("Convex Hull : " + str(ch))

    #ウィンドウの作成
    window = tkinter.Tk()
    window.title(u"Programing of Convex Hull by Gift-Wrapping.")
    window.geometry("600x600")

    #キャンバスの作成
    canvas = tkinter.Canvas(window, width = 600, height = 600)
    canvas.create_rectangle(0, 0, 600, 600, fill = 'black')
    canvas.place(x = 0, y = 0)

    #全ての点を表示
    for point in points:
        canvas.create_oval(point[0], point[1], point[0] + 5, point[1] + 5, fill = 'orange')

    #凸包に含まれる点に線を引く
    for i in range(0, len(ch)):
        #point[i]からpoint[j]に線を引くためにインデックスを計算
        j = i + 1
        if i == len(ch) - 1:
            j = 0
        #線を引く
        canvas.create_line(ch[i][0], ch[i][1], ch[j][0], ch[j][1], fill = 'sky blue')

    #ウィンドウを起動
    window.mainloop()
