def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:")
    print_array(arr)
    bubble_sort(arr)
    print("Отсортированный массив:")
    print_array(arr)