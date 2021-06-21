def binarysearch(arr: [int], to_find: int) -> bool:

    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:

        middle_index = left_index + (right_index - left_index) // 2
        current_element = arr[middle_index]

        if current_element == to_find:
            return True

        elif to_find > current_element:
            left_index = middle_index + 1

        elif to_find < current_element:
            right_index = middle_index - 1

    return False

if __name__ == "__main__":
    
    print("Enter the numbers in the list")
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    to_find = int(input("Enter the number to find\n"))
    isPresent = binarysearch(arr, to_find)
    if isPresent:
        print("Yes the Number is present in the list")
    else:
        print("Sorry, the Number is not present in the list")


