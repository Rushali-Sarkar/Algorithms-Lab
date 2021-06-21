def quicksort(arr: [int], starting_index: int, ending_index: int) -> [int]:

    if starting_index >= ending_index:
        return arr

    pivot_index = starting_index
    left_index = starting_index + 1
    right_index = ending_index

    while left_index <= right_index:

        if arr[left_index] > arr[pivot_index] and arr[right_index] < arr[pivot_index]:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

        elif arr[left_index] <= arr[pivot_index]:
            left_index += 1

        elif arr[right_index] >= arr[pivot_index]:
            right_index -= 1

    arr[right_index], arr[pivot_index] = arr[pivot_index], arr[right_index]
    arr = quicksort(arr, starting_index, right_index - 1)
    arr = quicksort(arr, right_index + 1, ending_index)
    return arr


if __name__ == "__main__":

    print("Enter the elements you wish to sort")
    arr = list(map(int, input().split()))
    print("The array after sorting is")
    arr = quicksort(arr, 0, len(arr) - 1)
    print(*arr)
