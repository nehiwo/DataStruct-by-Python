#insertion

def insertion_sort(arr, n):
    for i in range(0, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

if __name__ == "__main__":
    arr = [5, 9, 2, 1, 7, 3, 4, 6, 8, 0]
    print("prev arr : ", arr)

    insertion_sort(arr, len(arr))
    print("arr : ", arr)
