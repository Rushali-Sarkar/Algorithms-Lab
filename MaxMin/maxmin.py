def findmaxmin(arr: [int], maximum: int, minimum: int, start_index: int, end_index: int) -> (int, int):

    if len(arr) == 0:
        return maximum, minimum

    if start_index == end_index:
        if arr[start_index] > maximum:
            maximum = arr[start_index]
        if arr[start_index] < minimum:
            minimum = arr[start_index]
        return maximum, minimum

    middle_index = start_index + (end_index - start_index) // 2

    maximum, minimum = findmaxmin(arr, maximum, minimum, start_index, middle_index)
    maximum, minimum = findmaxmin(arr, maximum, minimum, middle_index + 1, end_index)
    return maximum, minimum


if __name__ == "__main__":

    print("Enter the elements in the array")
    arr = list(map(int, input().split()))
    maximum, minimum = findmaxmin(arr, float('-inf'), float('inf'), 0, len(arr) - 1)
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
