#include <iostream>
#include <vector>

using namespace std;

void swap(int& number1, int& number2) {

    int temp = number1;
    number1 = number2;
    number2 = temp;
    return;

}

void print(vector<int>& arr) {

    for (int i = 0; i < arr.size(); i++)
        cout << arr[i] << '\t';
    cout << endl;
    return;

}

vector<int> quicksort(vector<int>& arr, int starting_index, int ending_index) {

    if (starting_index >= ending_index)
        return arr;

    int pivot_index = starting_index;
    int left_index = starting_index + 1;
    int right_index = ending_index;

    while (left_index <= right_index) {

        if (arr[pivot_index] < arr[left_index] && arr[pivot_index] > arr[right_index])
            swap(arr[left_index], arr[right_index]);
        else if (arr[pivot_index] >= arr[left_index])
            left_index++;
        else if (arr[pivot_index] <= arr[right_index])
            right_index--;

    }
    swap(arr[right_index], arr[pivot_index]);
    arr = quicksort(arr, starting_index, right_index - 1);
    arr = quicksort(arr, right_index + 1, ending_index);
    return arr;
}

int main(int argc, char* argv[]) {

    int size;
    cout << "Enter the elements you want in the array" << endl;
    cin >> size;
    cout << "Enter " << size << " elements" << endl;
    vector<int> arr;
    int current_number;
    for (int i = 0; i < size; i++) {
        cin >> current_number;
        arr.push_back(current_number);
    }
    arr = quicksort(arr, 0, size - 1);
    cout << "The numbers after sorting are" << endl;
    print(arr);
    return 0;
}
        
