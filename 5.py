def shell_sort(arr):
    n = len(arr)
    
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    print("Исходный массив:", end=" ")
    print_array(arr)
    shell_sort(arr)
    print("Отсортированный массив:", end=" ")
    print_array(arr)