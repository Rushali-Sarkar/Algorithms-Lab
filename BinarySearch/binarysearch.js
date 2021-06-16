function binarysearch(arr, to_find) {

    var left_index = 0;
    var right_index = arr.length - 1;

    while (left_index <= right_index) {

        var middle_index = left_index + parseInt((right_index - left_index) / 2);
        var current_number = arr[middle_index];

        if (to_find === current_number) {
            return true;
        }

        else if (to_find < current_number) {
            right_index = middle_index - 1;
        }
        
        else if (to_find > current_number) {
            left_index = middle_index + 1;
        }
    }

    return false;
}

const readline = require("readline-sync");
let size = parseInt(readline.question("Enter the size of the array you wish to enter\n"));
console.log("Enter ", size, " numbers");
let arr = []
for (var i = 0; i < size; i++)
    arr.push(parseInt(readline.question()));
arr.sort();
console.log("Enter the number to find");
let to_find = parseInt(readline.question());
let isPresent = Boolean(binarysearch(arr, to_find));
if (isPresent) {
    console.log("Yes, the number is present in the array");
}
else {
    console.log("Sorry, the number is not present in the array");
}
