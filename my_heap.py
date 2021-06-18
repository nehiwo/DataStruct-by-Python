# -*- coding: utf-8 -*-
#my_heap

import math

#無限大の定義
INFTY = 2**31 - 1

#スワップ関数
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

class MyHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_max_heap()

    #最大ヒープ化
    def max_heapify(self, index):
        #arr[index],arr[left],arr[right]の中から一番大きな値を持つ節点を調べる
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = index
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right

        #節点の交換とヒープ化
        if largest != index:
            swap(self.arr, index, largest)
            self.max_heapify(largest)

    #最大ヒープの生成
    def create_max_heap(self):
        self.size = len(self.arr)
        for i in range(int(math.floor(self.size / 2) - 1), -1, -1):
            self.max_heapify(i)

    #親のインデックスを取得
    def get_parent(self, index):
        return int(math.floor(self.size / 2) - 1)

    #左の子のインデックスを取得
    def get_left(self, index):
        return 2 * (index + 1) - 1

    #右の子のインデックスを取得
    def get_right(self, index):
        return 2 * (index + 1)

    #取得
    def extract_max(self):
        #ヒープが空の場合
        if self.size < 1:
            print("ヒープは空です。")
            return None

        #要素の取り出しとヒープ化
        max = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.arr.pop(self.size - 1)
        self.size -= 1
        self.max_heapify(0)

        return max

    #挿入
    def insert(self, val):
        self.size += 1
        self.arr.append(-INFTY)
        self.increase_val(self.size - 1, val)

    #優先度の更新
    def increase_val(self, index, val):
        #現在値より値が小さい場合
        if self.arr[index] > val:
            print("値が増えていません。")
            return None
        else:
            self.arr[index] = val
            while self.arr[index] > self.arr[self.get_parent(index)] and index > 0:
                swap(self.arr, index, self.get_parent(index))
                index = self.get_parent(index)

    #ヒープソート
    def heap_sort(self):
        #ソート
        for i in range(self.size - 1, 0, -1):
            swap(self.arr, 0, i)
            self.size -= 1
            self.max_heapify(0)

        #ヒープの大きさを配列の大きさに戻す
        self.size = len(self.arr)

    #文字列に変換
    def to_string(self):
        return str(self.arr[:self.size])

if __name__ == "__main__":
    #ランダムな配列を生成
    arr = [6, 3, 18, 8, 1, 13]
    my_heap = MyHeap(arr)
    print("My Heap : " + my_heap.to_string())

    #先頭要素を取得
    x = my_heap.extract_max()
    print("the Gotten Elemnt : " + str(x))
    print("My Heap : " + my_heap.to_string())

    #新たな要素として整数値１０を挿入
    my_heap.insert(10)
    print("My Heap : " + my_heap.to_string())

    #ソート
    my_heap.heap_sort()
    print("My Heap : " + my_heap.to_string())
