#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool binarysearch(vector<int> arr, int to_find) {

    int left_index = 0;
    int right_index = arr.size() - 1;

    while (left_index <= right_index) {

        int middle_index = left_index + (right_index - left_index) / 2;
        int current_number = arr[middle_index];

        if (current_number == to_find)
            return true;

        else if (to_find < current_number)
            right_index = middle_index - 1;

        else if (to_find > current_number)
            left_index = middle_index + 1;
    }
    return false;
}

int main(int argc, char* argv[]) {

    cout << "Enter the number of number you wish to enter in the array" << endl;
    int size;
    cin >> size;
    cout << "Enter " << size << " numbers" << endl;
    vector<int> arr;
    for (int i = 0; i < size; i++) {
        int current_number;
        cin >> current_number;
        arr.push_back(current_number);
    }
    sort(arr.begin(), arr.end());
    cout << "Enter the number you wish to find" << endl;
    int to_find;
    cin >> to_find;
    bool isPresent = binarysearch(arr, to_find);
    if (isPresent)
        cout << "Yes the number is present in the list" << endl;
    else
        cout << "Sorry the number is not present in the list" << endl;
    
    return 0;
}
