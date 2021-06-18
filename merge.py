#mergesort
# -*- coding: utf-8 -*-
import math

#無限大の定義
INFTY = 2**31 - 1

#merge(統治)
def merge(arr, p, q, r):
    n = q - p + 1
    m = r - q
    left = [INFTY] * (n + 1)
    right = [INFTY] * (m + 1)

    for i in range(0, n):
        left[i] = arr[p + i]
    for j in range(0, m):
        right[j] = arr[q + 1 + j]
    #print(left,right)

    i = j = 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    #print(arr)

#mergesort(分割→統治)
def merge_sort(arr, p, r):
    if p < r:
        q = int(math.floor((p + r) / 2))
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

if __name__ == "__main__":
    arr = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
    print("prev arr : ", arr)

    merge_sort(arr, 0, len(arr) - 1)
    print("arr : ", arr)
