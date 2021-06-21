#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <stdbool.h>

bool binarysearch(int* arr, int size, int to_find) {

    int left_index = 0;
    int right_index = size - 1;

    while (left_index <= right_index) {

        int middle_index = left_index + (right_index - left_index) / 2;
        int current_element = arr[middle_index];

        if (to_find == current_element)
            return true;

        else if (to_find < current_element)
            right_index = middle_index - 1;

        else if (to_find > current_element)
            left_index = middle_index + 1;

    }

    return false;
}

int compare(const void* number1, const void* number2) {
       return ( *(int*)number1 - *(int*)number2 );
}

int main(int argc, char* argv[]) {

    int size;
    printf("Enter the number of elements you want in the array\n");
    scanf("%d", &size);
    printf("Enter %d elements\n" , size);
    int* arr = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        int current_element;
        scanf("%d", &current_element);
        arr[i] = current_element;
    }
    qsort(arr, size, sizeof(int), compare);
    printf("Enter the number you want to find\n");
    int to_find;
    scanf("%d", &to_find);
    bool isPresent = binarysearch(arr, size, to_find);
    if (isPresent)
        printf("Yes the number is present in the list\n");
    else
        printf("No the number is not present in the list\n");
    return 0;
}


