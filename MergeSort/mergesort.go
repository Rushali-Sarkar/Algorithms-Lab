package main

import "fmt"

func printArray(arr []int) {
    for i := 0; i < len(arr); i++ {
        fmt.Print(arr[i], "\t")
    }
    fmt.Println()
    return
}

func merge(arr1 []int, arr2 []int) ([]int) {

    pointer1 := 0
    pointer2 := 0

    size1 := len(arr1)
    size2 := len(arr2)

    mergedarr := []int{}

    for pointer1 < size1 && pointer2 < size2 {

        number1 := arr1[pointer1]
        number2 := arr2[pointer2]

        if number1 < number2 {
            mergedarr = append(mergedarr, number1)
            pointer1++;
        } else if number2 <= number1 {
            mergedarr = append(mergedarr, number2)
            pointer2++
        }
    }
    for pointer1 < size1 {
        mergedarr = append(mergedarr, arr1[pointer1])
        pointer1++
    }
    for pointer2 < size2 {
        mergedarr = append(mergedarr, arr2[pointer2])
        pointer2++
    }

    return mergedarr
}

func mergesort(arr []int) ([]int){

    if len(arr) <= 1 {
        return arr
    }
    middle_index := int(len(arr) / 2)
    left_arr := arr[: middle_index]
    right_arr := arr[middle_index: ]
    return merge(mergesort(left_arr), mergesort(right_arr))
}

func main() {

    var size int
    fmt.Println("Enter the number of elements you want to enter in the array")
    fmt.Scanln(&size)
    fmt.Println("Enter ", size, " numbers")
    arr := []int{}
    for i := 0; i < size; i++ {
        var current_number int
        fmt.Scanln(&current_number)
        arr = append(arr, current_number)
    }
    arr = mergesort(arr)
    fmt.Println("The array after is sorting is")
    printArray(arr)
    return
}






