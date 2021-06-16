package main

import "fmt"
import "sort"

func binarysearch(arr []int, left_index int, right_index int, to_find int) (bool) {

    for left_index <= right_index {

        middle_index := left_index + (right_index - left_index) / 2

        if arr[middle_index] == to_find {
            return true
        }

        if arr[middle_index] > to_find {
            right_index = middle_index - 1
        }

        if arr[middle_index] < to_find {
            left_index = middle_index + 1
        }
    }
    return false
}

func main() {

    fmt.Println("Enter the number of elements you want to enter in the array")
    var size int
    fmt.Scanln(&size)
    fmt.Println("Enter ",  size,  " numbers")
    arr := make([]int, size)
    for i := 0; i < size; i++ {
        fmt.Scanln(&arr[i])
    }
    sort.Ints(arr)
    fmt.Println("Enter the number you want to search for")
    var to_find int
    fmt.Scanln(&to_find)
    isPresent := binarysearch(arr, 0, size - 1, to_find)
    if isPresent {
        fmt.Println("Yes, the number is present in the list")
    } else {
        fmt.Println("Sorry, the number is not present in the list")
    }
    return
}
