#include <iostream>
#include <vector>

using namespace std;


void print(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << '\t';
    cout << endl;
    return;
}

vector<int> merge(vector<int> arr1, vector<int> arr2) {

    int size1 = arr1.size();
    int size2 = arr2.size();

    int pointer1 = 0;
    int pointer2 = 0;

    vector<int> mergedarr;

    while (pointer1 < size1 && pointer2 < size2) {

        int number1 = arr1[pointer1];
        int number2 = arr2[pointer2];

        if (number1 < number2) {
            mergedarr.push_back(number1);
            pointer1 += 1;
        }

        else {
            mergedarr.push_back(number2);
            pointer2 += 1;
        }
    }

    while (pointer1 < size1) {
        mergedarr.push_back(arr1[pointer1]);
        pointer1 += 1;
    }
    while (pointer2 < size2) {
        mergedarr.push_back(arr2[pointer2]);
        pointer2 += 1;
    }

    return mergedarr;
}

vector<int> initialize(vector<int> arr, int start_index, int limit) {
    vector<int> new_arr;
    for (int i = start_index; i < limit; i++)
        new_arr.push_back(arr[i]);
    return new_arr;
}

vector<int> mergesort(vector<int> arr) {

    if (arr.size() <= 1)
        return arr;
    int middle_index = arr.size() / 2;
    vector<int> left_arr = initialize(arr, 0, middle_index);
    vector<int> right_arr = initialize(arr, middle_index, arr.size());
    return merge(mergesort(left_arr), mergesort(right_arr));
}


int main(int argc, char* argv[]) {

    int size;
    cout << "Enter the number of elements you want in the arr" << endl;
    cin >> size;
    cout << "Enter " << size << " elements" << endl;
    vector<int> arr;
    for (int i = 0; i < size; i++) {
        int current_number;
        cin >> current_number;
        arr.push_back(current_number);
    }
    arr = mergesort(arr);
    cout << "The array after sorting is" << endl;
    print(arr);
    return 0;

}
