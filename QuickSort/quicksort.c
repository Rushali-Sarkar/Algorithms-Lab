#include <stdio.h>
#include <malloc.h>


void print(int* arr, int size) {

    for (int i = 0; i < size; i++)
        printf("%d\t", arr[i]);
    printf("\n");
    return;
}

void swap(int* number1, int* number2) {
    
    int temp = *number1;
    *number1 = *number2;
    *number2 = temp;
    return;

}

int* quicksort(int* arr, int starting_index, int ending_index) {

    if (starting_index >= ending_index)
        return arr;

    int pivot_index = starting_index;
    int left_index = starting_index + 1;
    int right_index = ending_index;

    while (left_index <= right_index) {

        if (arr[pivot_index] < arr[left_index] && arr[pivot_index] > arr[right_index])
            swap(&arr[left_index], &arr[right_index]);
        else if (arr[left_index] <= arr[pivot_index])
            left_index += 1;
        else if (arr[right_index] >= arr[pivot_index])
            right_index -= 1;

    }
    swap(&arr[right_index], &arr[pivot_index]);
    arr = quicksort(arr, starting_index, right_index - 1);
    arr = quicksort(arr, right_index + 1, ending_index);
    return arr;
}

int main(int argc, char* argv[]) {

    int size;
    printf("Enter the number of elements you wish to sort\n");
    scanf("%d", &size);
    int* arr = malloc(sizeof(int) * size);
    printf("Enter %d numbers\n", size);
    int current_number;
    for (int i = 0; i < size; i++) {
        scanf("%d", &current_number);
        arr[i] = current_number;
    }
    printf("Came here\n");
    arr = quicksort(arr, 0, size - 1);
    print(arr, size);
    return 0;
}

