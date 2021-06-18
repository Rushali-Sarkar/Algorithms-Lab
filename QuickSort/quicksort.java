import java.util.*;

class quicksort {

    public static void print(ArrayList<Integer> arr) {
        for (int i = 0; i < arr.size(); i++)
            System.out.print(arr.get(i) + "\t");
        System.out.println();
        return;
    }

    public static ArrayList<Integer> quicksort(ArrayList<Integer> arr, int starting_index, int ending_index) {

        if (starting_index >= ending_index) 
            return arr;

        int pivot_index = starting_index;
        int left_index = starting_index + 1;
        int right_index = ending_index;

        while (left_index <= right_index) {

            if (arr.get(pivot_index) > arr.get(right_index) && arr.get(pivot_index) < arr.get(left_index)) {
                int temp = arr.get(left_index);
                arr.set(left_index, arr.get(right_index));
                arr.set(right_index, temp);
            }
            else if (arr.get(left_index) <= arr.get(pivot_index))
                left_index++;
            else if (arr.get(right_index) >= arr.get(pivot_index))
                right_index--;
        }

        int temp = arr.get(pivot_index);
        arr.set(pivot_index, arr.get(right_index));
        arr.set(right_index, temp);

        arr = quicksort(arr, starting_index, right_index - 1);
        arr = quicksort(arr, right_index + 1, ending_index);
        return arr;
    }

    public static void main(String args[]) {

        Scanner ob = new Scanner(System.in);
        System.out.println("Enter the size of the array");
        int size = ob.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        System.out.println("Enter " + size + " elements");
        for (int i = 0; i < size; i++)
            arr.add(ob.nextInt());
        System.out.println("The elements of the array after sorting are");
        arr = quicksort(arr, 0, size - 1);
        print(arr);
        return;
    }
}
