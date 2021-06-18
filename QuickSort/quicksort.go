package main

import "fmt"

func quicksort(arr []int, starting_index int, ending_index int)  ([]int) {

    if starting_index >= ending_index {
        return arr;
    }

    pivot_index := starting_index
    left_index := starting_index + 1
    right_index := ending_index

    for left_index <= right_index {

        if arr[pivot_index] < arr[left_index] && arr[pivot_index] > arr[right_index] {
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        } else if arr[pivot_index] >= arr[left_index] {
            left_index++
        } else if arr[pivot_index] <= arr[right_index] {
            right_index--;
        }
    }
    arr[pivot_index], arr[right_index] = arr[right_index], arr[pivot_index]
    arr = quicksort(arr, starting_index,  right_index - 1)
    arr = quicksort(arr, right_index + 1, ending_index)
    return arr
}

func main() {

    var size int
    fmt.Println("Enter the size of the array")
    fmt.Scanln(&size)
    fmt.Println("Enter ", size, " numbers")
    arr := []int{}
    for i := 0; i < size; i++ {
        var current_number int
        fmt.Scanln(&current_number)
        arr = append(arr, current_number)
    }
    fmt.Println("The array after sorting is")
    arr = quicksort(arr, 0, size - 1)
    fmt.Println(arr)
    return
}

