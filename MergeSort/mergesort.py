def merge(arr1: [int], arr2: [int]) -> [int]:

    pointer1 = 0
    pointer2 = 0

    length1 = len(arr1)
    length2 = len(arr2)

    mergedarr = []

    while pointer1 < length1 and pointer2 < length2:

        number1 = arr1[pointer1] 
        number2 = arr2[pointer2]

        if number1 < number2:
            mergedarr.append(number1)
            pointer1 += 1
        else:
            mergedarr.append(number2)
            pointer2 += 1

    while pointer1 < length1:
        mergedarr.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 < length2:
        mergedarr.append(arr2[pointer2])
        pointer2 += 1

    return mergedarr

def mergesort(arr: [int]) -> [int]:

    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_half = arr[: middle_index]
    right_half = arr[middle_index: ]
    return merge(mergesort(left_half), mergesort(right_half))

if __name__ == "__main__":

    print("Enter the elements of the list")
    arr = list(map(int, input().split()))
    arr = mergesort(arr)
    print("The array after sorting: ")
    print(*arr)

