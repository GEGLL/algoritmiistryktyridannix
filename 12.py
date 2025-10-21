def shell_sort_advanced(arr):
    n = len(arr)
    
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # Последовательность Циура
    
    for gap in gaps:
        if gap > n:
            continue
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3, 8, 15, 27, 33, 11]
    print("Исходный массив:", arr)
    shell_sort_advanced(arr)
    print("Отсортированный массив:", arr)