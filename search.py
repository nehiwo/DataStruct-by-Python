#search

import math
import quick
import time
import random

class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key

    #liner search
    def liner(self):
        for i in range(0, len(self.arr)):
            if self.arr[i] == self.key:
                return i
        return None

    def binary(self, p, r):
        if r < p:
            return None
        else:
            q = int(math.floor((p + r) / 2))
            if self.arr[q] > self.key:
                return binary(p, q - 1)
            elif self.arr[q] < self.key:
                return binary(q + 1, r)
            else:
                return q

if __name__ == "__main__":
    arr = []
    N = 1000000
    for i in range(0, N):
        arr.append(random.uniform(0, 10000000))
    print("create an arr.")

    temp = arr[921433]

    key = temp
    search = Search(arr, key)
    start = time.time()
    index = search.liner()
    end = time.time()
    if index != None:
        print(str(key) + " is in the arr[" + str(index) + "].")
    else:
        print(str(key) + " is not this arr.")
    print("search time : " + str(end - start))

    key = 78
    search = Search(arr, key)
    start = time.time()
    index = search.liner()
    end = time.time()
    if index != None:
        print(str(key) + " is in the arr[" + str(index) + "].")
    else:
        print(str(key) + " is not this arr.")
    print("search time : " + str(end - start))

    quick.quick_sort(arr, 0, len(arr) - 1)
    print("sort the arr.")

    key = temp
    search = Search(arr, key)
    start = time.time()
    index = search.liner()
    end = time.time()
    if index != None:
        print(str(key) + " is in the arr[" + str(index) + "].")
    else:
        print(str(key) + " is not this arr.")
    print("search time : " + str(end - start))

    key = 78
    search = Search(arr, key)
    start = time.time()
    index = search.liner()
    end = time.time()
    if index != None:
        print(str(key) + " is in the arr[" + str(index) + "].")
    else:
        print(str(key) + " is not this arr.")
    print("search time : " + str(end - start))
