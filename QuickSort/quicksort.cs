using System;
using System.Collections;


class sort {

    static public void print(ArrayList arr) {

        int size = arr.Count;
        for (int i = 0; i < size; i++)
            Console.Write("{0}\t", (int)arr[i]);
        Console.WriteLine();
        return;
    }

    static public ArrayList quicksort(ArrayList arr, int starting_index, int ending_index) {

        if (starting_index >= ending_index)
            return arr;

        int pivot_index = starting_index;
        int left_index = starting_index + 1;
        int right_index = ending_index;

        while (left_index <= right_index) {

            if ((int)arr[left_index] > (int)arr[pivot_index] && (int)arr[right_index] < (int)arr[pivot_index]) {

                int temp = (int)arr[left_index];
                arr[left_index] = arr[right_index];
                arr[right_index] = temp;
            }
            else if ((int)arr[left_index] <= (int)arr[pivot_index])
                left_index++;
            else if((int)arr[right_index] >= (int)arr[pivot_index])
                right_index--;
            
        }
        int temporary = (int)arr[right_index];
        arr[right_index] = arr[pivot_index];
        arr[pivot_index] = temporary;

        arr = quicksort(arr, starting_index, right_index - 1);
        arr = quicksort(arr, right_index + 1, ending_index);
        return arr;
    }

    static public void Main(String[] args) {

        Console.WriteLine("Enter the size of the array");
        int size = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter {0} numbers", size);
        ArrayList arr = new ArrayList();
        for (int i = 0; i < size; i++) 
            arr.Add(Convert.ToInt32(Console.ReadLine()));
        Console.WriteLine("The array after sorting is");
        arr = quicksort(arr, 0, size - 1);
        print(arr);
        return;
    }
}



