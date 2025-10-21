public class SelectionSort {
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
    
    public static void main(String[] args) {
        int[] testArray = {64, 25, 12, 22, 11};
        System.out.print("Исходный массив: ");
        printArray(testArray);
        selectionSort(testArray);
        System.out.print("Отсортированный массив: ");
        printArray(testArray);
    }
    
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}