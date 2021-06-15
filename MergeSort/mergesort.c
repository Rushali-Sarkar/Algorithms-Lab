#include <stdio.h>
#include <malloc.h>

void print(int* arr, int size) {

    for (int i = 0; i < size; i++)
        printf("%d\t", arr[i]);
    printf("\n");
    return;
}

int* merge(int* arr1, int size1, int* arr2, int size2) {

    int* mergedarr = malloc(sizeof(int) * (size1 + size2));
    int pointer1 = 0;
    int pointer2 = 0;
    int pointer3 = 0;

    while (pointer1 < size1 && pointer2 < size2) {

        int number1 = arr1[pointer1];
        int number2 = arr2[pointer2];

        if (number1 < number2) {
            mergedarr[pointer3] = number1;
            pointer1++;
            pointer3++;
        }
        else if (number2 <= number1) {
            mergedarr[pointer3] = number2;
            pointer2++;
            pointer3++;
        }
    }

    while (pointer1 < size1) {
        mergedarr[pointer3] = arr1[pointer1];
        pointer1++;
        pointer3++;
    }

    while (pointer2 < size2) {
        mergedarr[pointer3] = arr2[pointer2];
        pointer2++;
        pointer3++;
    }

    return mergedarr;
}

int* initialize(int* arr, int start_index, int limit) {
    
    int* new_arr = malloc(sizeof(int) * (limit - start_index));
    int pointer = 0;
    for (int i = start_index; i < limit; i++) {
        new_arr[pointer] = arr[i];
        pointer++;
    }
    return new_arr;
}

int* mergesort(int* arr, int size) {

    if (size <= 1)
        return arr;

    int middle_index = size / 2;
    int* left_arr = initialize(arr, 0, middle_index);
    int* right_arr = initialize(arr, middle_index, size);
    return merge(mergesort(left_arr, middle_index), middle_index, mergesort(right_arr, size - middle_index), size - middle_index);
}

int main(int argc, char* argv[]) {

    int size;
    printf("Enter the number of elements you want to enter in the array\n");
    scanf("%d", &size);
    printf("Enter %d elements\n");
    int* arr = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        int current_number;
        scanf("%d", &current_number);
        arr[i] = current_number;
    }
    arr = mergesort(arr, size);
    printf("The numbers after sorting are\n");
    print(arr, size);
    return 0;
}
