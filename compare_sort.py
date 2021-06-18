import insertion
import bubble
import merge
import quick
import random
import time
import copy

if __name__ == "__main__":
    arr = []
    N = 10000
    for i in range(0, N):
        arr.append(random.uniform(0, 10000000))

    start = time.time()
    insertion.insertion_sort(copy.copy(arr), N)
    end = time.time()
    print("insertion time : ", end - start)

    start = time.time()
    bubble.bubble_sort(copy.copy(arr), N)
    end = time.time()
    print("bubble time : ", end - start)

    start = time.time()
    merge.merge_sort(copy.copy(arr), 0, N - 1)
    end = time.time()
    print("merge time : ", end - start)

    start = time.time()
    quick.quick_sort(arr, 0, N - 1)
    end = time.time()
    print("quick time : ", end - start)

    for i in range(0, 51):
        bubble.swap(arr, int(random.uniform(0, 9999)), int(random.uniform(0, 9999)))

    start = time.time()
    insertion.insertion_sort(copy.copy(arr), N)
    end = time.time()
    print("insertion time : ", end - start)

    start = time.time()
    bubble.bubble_sort(copy.copy(arr), N)
    end = time.time()
    print("bubble time : ", end - start)

    start = time.time()
    merge.merge_sort(copy.copy(arr), 0, N - 1)
    end = time.time()
    print("merge time : ", end - start)

    start = time.time()
    quick.quick_sort(arr, 0, N - 1)
    end = time.time()
    print("quick time : ", end - start)
