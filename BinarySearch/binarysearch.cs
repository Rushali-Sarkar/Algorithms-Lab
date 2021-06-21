using System;
using System.Collections;

class search {

    static public bool binarysearch(ArrayList arr, int to_find) {

        int left_index = 0;
        int right_index = arr.Count - 1;

        while (left_index <= right_index) {

            int middle_index = left_index + (int)(right_index - left_index) / 2;
            int current_number = (int)arr[middle_index];

            if (current_number == to_find)
                return true;
            
            else if (current_number < to_find)
                left_index = middle_index + 1;

            else if (current_number > to_find)
                right_index = middle_index - 1;
        }

        return false;
    }

    static public void Main(String[] args) {

        Console.WriteLine("Enter the number of elements you want to add in the list");
        int size = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter {0} numbers", size);
        ArrayList arr = new ArrayList();
        for (int i = 0; i < size; i++)
            arr.Add(Convert.ToInt32(Console.ReadLine()));
        arr.Sort();
        Console.WriteLine("Enter the number you wish to find");
        int to_find = Convert.ToInt32(Console.ReadLine());
        bool isPresent = binarysearch(arr, to_find);
        if (isPresent)
            Console.WriteLine("Yes, the number is present in the list");
        else
            Console.WriteLine("Sorry, the number is not present in the list");
        return;
    }
}
