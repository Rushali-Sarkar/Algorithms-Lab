#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void findmaxmin(int* arr, int starting_index, int ending_index, int* maximum, int* minimum) {

    if (starting_index > ending_index)
        return;

    if (starting_index == ending_index) {

        if (arr[starting_index] > *maximum)
            *maximum = arr[starting_index];
        if (arr[starting_index] < *minimum)
            *minimum = arr[starting_index];

        return;
    }

    int middle_index = starting_index + (ending_index - starting_index) / 2;
    findmaxmin(arr, starting_index, middle_index, maximum, minimum);
    findmaxmin(arr, middle_index + 1, ending_index, maximum, minimum);
    return;
}

int main(int argc, char* argv[]) {

    printf("Enter the number of elements you wish to enter in the list\n");
    int size;
    scanf("%d", &size);
    printf("Enter %d numbers\n", size);
    int* arr = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        int current_number;
        scanf("%d", &current_number);
        arr[i] = current_number;
    }
    int maximum = INT_MIN;
    int minimum = INT_MAX;
    findmaxmin(arr, 0, size - 1, &maximum, &minimum);
    printf("Maximum: %d\n", maximum);
    printf("Minimum: %d\n", minimum);
    return 0;
}
