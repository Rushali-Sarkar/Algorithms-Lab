function merge(arr1, arr2) {

    var pointer1 = 0;
    var pointer2 = 0;

    var size1 = arr1.length;
    var size2 = arr2.length;

    let mergedarr = []

    while (pointer1 < size1 && pointer2 < size2) {

        var number1 = arr1[pointer1];
        var number2 = arr2[pointer2];

        if (number1 < number2) {
            mergedarr.push(number1);
            pointer1++;
        }

        else {
            mergedarr.push(number2);
            pointer2++;
        }
    }
    while (pointer1 < size1) {
        mergedarr.push(arr1[pointer1]);
        pointer1++;
    }
    while (pointer2 < size2) {
        mergedarr.push(arr2[pointer2]);
        pointer2++;
    }
    return mergedarr;
}

function mergesort(arr) {

    if (arr.length <= 1)
        return arr;

    var middle_index = parseInt(arr.length / 2);
    let left_arr = arr.slice(0, middle_index);
    let right_arr = arr.slice(middle_index);
    return merge(mergesort(left_arr), mergesort(right_arr));
}

const readline = require("readline-sync");
console.log("Enter number of elements you want to add in the array");
let size = parseInt(readline.question());
console.log("Enter ", size, " numbers");
let arr = []
for (var i = 0; i < size; i++)
    arr.push(parseInt(readline.question()));
arr = mergesort(arr);
console.log("The array after sorting is");
console.log(arr);

