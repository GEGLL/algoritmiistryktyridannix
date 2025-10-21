def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

def print_array(array):
    for value in array:
        print(value, end=" ")
    print()

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print("Исходный массив:")
    print_array(array)
    insertion_sort(array)
    print("Отсортированный массив:")
    print_array(array)