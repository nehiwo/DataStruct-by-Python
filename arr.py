#array
import array

N = 10

def insert(arr, index, val):
	for i in range(N - 1, index, -1):
		arr[i] = arr[i - 1]
	arr[index] = val

def delete(arr, index):
	for i in range(index, N - 1):
		arr[i] = arr[i + 1]
	arr[N - 1] = -1

if __name__ == "__main__":
	arr = array.array('i', [1, 2, 3, 4, 5, 6, -1, -1, -1, -1])
	print(arr)
	print(arr[2])
	insert(arr, 8, 9)
	print(arr)
	delete(arr, 8)
	print(arr)
