#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

void findmaxmin(vector<int>& arr, int starting_index, int ending_index, int& maximum, int& minimum) {

    if (arr.size() == 0)
        return;

    if (starting_index == ending_index) {
        if (arr[starting_index] > maximum)
            maximum = arr[starting_index];

        if (arr[starting_index] < minimum)
            minimum = arr[starting_index];
        return;

    }

    int middle_index = starting_index + (ending_index - starting_index) / 2;
    findmaxmin(arr, starting_index, middle_index, maximum, minimum);
    findmaxmin(arr, middle_index + 1, ending_index, maximum, minimum);
    return;
}

int main(int argc, char* argv[]) {

    cout << "Enter the number of elements you wish to enter in the array" << endl;
    int size;
    cin >> size;
    cout << "Enter " << size << " elements" << endl;
    vector<int> arr;
    for (int i = 0; i < size; i++) {
        int current_element;
        cin >> current_element;
        arr.push_back(current_element);
    }
    int maximum = INT_MIN;
    int minimum = INT_MAX;
    findmaxmin(arr, 0, size - 1, maximum, minimum);
    cout << "Maximum: " << maximum << endl;
    cout << "Minimum: " << minimum << endl;
    return 0;
}