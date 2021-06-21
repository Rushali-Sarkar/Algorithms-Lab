using System;
using System.Collections;

class MergeSort {

    static public void print(ArrayList arr) {
        int size = arr.Count;
        for (int i = 0; i < size; i++)
            Console.Write("{0}\t", arr[i]);
        Console.WriteLine();
        return;
    }

    static public ArrayList initialize(ArrayList arr, int start_index, int limit) {
        ArrayList new_arr = new ArrayList();
        for (int i = start_index; i < limit; i++)
            new_arr.Add((int)arr[i]);
        return new_arr;
    }

    static public ArrayList merge(ArrayList arr1, ArrayList arr2) {
        
        int pointer1 = 0;
        int pointer2 = 0;
        int size1 = arr1.Count;
        int size2 = arr2.Count;
        ArrayList mergedarr = new ArrayList();

        while (pointer1 < size1 && pointer2 < size2) {

            int number1 = (int)arr1[pointer1];
            int number2 = (int)arr2[pointer2];

            if (number1 <= number2) {
                mergedarr.Add(number1);
                pointer1++;
            }
            else if (number2 < number1) {
                mergedarr.Add(number2);
                pointer2++;
            }
        }

        while (pointer1 < size1) {
            mergedarr.Add((int)arr1[pointer1]);
            pointer1++;
        }
        while (pointer2 < size2) {
            mergedarr.Add((int)arr2[pointer2]);
            pointer2++;
        }

        return mergedarr;
    }

    static public ArrayList mergesort(ArrayList arr) {

        if (arr.Count <= 1)
            return arr;

        ArrayList left_arr = new ArrayList();
        ArrayList right_arr = new ArrayList();
        int middle_index = (int)(arr.Count) / 2;
        left_arr = initialize(arr, 0, middle_index);
        right_arr = initialize(arr, middle_index, arr.Count);
        return merge(mergesort(left_arr), mergesort(right_arr));
    }

    static public void Main(String[] args) {

        Console.WriteLine("Enter the number of elements you want to enter in the array");
        int size = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter {0} numbers", size);
        ArrayList arr = new ArrayList();
        for (int i = 0; i < size; i++)
            arr.Add(Convert.ToInt32(Console.ReadLine()));
        arr = mergesort(arr);
        Console.WriteLine("The array after sorting is");
        print(arr);
        return;
    }
}




