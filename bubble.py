#bubblesort

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)

if __name__ == "__main__":
        arr = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
        print("prev arr : ", arr)

        bubble_sort(arr, len(arr))
        print("arr : ", arr)
