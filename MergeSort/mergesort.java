import java.util.*;

class mergesort {

    public static void print(ArrayList<Integer> arr) {
        for (int i = 0; i < arr.size(); i++)
            System.out.print(arr.get(i) + "\t");
        System.out.println();
        return;
    }

    public static ArrayList<Integer> initialize(ArrayList<Integer> arr, int start_index, int limit) {

        ArrayList<Integer> new_arr = new ArrayList<Integer>();
        for (int i = start_index; i < limit; i++)
            new_arr.add(arr.get(i));
        return new_arr;
    }

    public static ArrayList<Integer> merge(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {

        int pointer1 = 0;
        int pointer2 = 0;

        int size1 = arr1.size();
        int size2 = arr2.size();

        ArrayList<Integer> mergedarr = new ArrayList<Integer>();

        while (pointer1 < size1 && pointer2 < size2) {

            int number1 = arr1.get(pointer1);
            int number2 = arr2.get(pointer2);

            if (number1 <= number2) {
                mergedarr.add(number1);
                pointer1++;
            }

            else if (number2 < number1) {
                mergedarr.add(number2);
                pointer2++;
            }
        }

        while (pointer1 < size1) {
            mergedarr.add(arr1.get(pointer1));
            pointer1++;
        }

        while (pointer2 < size2) {
            mergedarr.add(arr2.get(pointer2));
            pointer2++;
        }

        return mergedarr;
    }

    public static ArrayList<Integer> mergesort(ArrayList<Integer> arr) {
        if (arr.size() <= 1)
            return arr;
        
        int middle_index = arr.size() / 2;
        ArrayList<Integer> left_arr = new ArrayList<Integer>();
        ArrayList<Integer> right_arr = new ArrayList<Integer>();
        left_arr = initialize(arr, 0, middle_index);
        right_arr = initialize(arr, middle_index, arr.size());
        return merge(mergesort(left_arr), mergesort(right_arr));
    }

    public static void main(String args[]) {

        Scanner ob = new Scanner(System.in);
        System.out.println("Enter the number of elements you want in the array");
        int size = ob.nextInt();
        System.out.println("Enter " + size + " elements");
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < size; i++)
            arr.add(ob.nextInt());
        ob.close();
        arr = mergesort(arr);
        System.out.println("The numbers after sorting are");
        print(arr);
        return;
    }
}