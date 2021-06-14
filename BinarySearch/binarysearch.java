import java.util.*;

class binarysearch {

    public static boolean binarysearch(ArrayList<Integer> arr, int to_find) {

        int left_index = 0;
        int right_index = arr.size() - 1;

        while (left_index <= right_index) {

            int middle_index = left_index + (right_index - left_index) / 2;
            int current_element = arr.get(middle_index);
            
            if (current_element == to_find)
                return true;

            else if (to_find < current_element)
                right_index = middle_index - 1;

            else if (to_find > current_element)
                left_index = middle_index + 1;
        }

        return false;
    }

    public static void main(String args[]) {

        Scanner ob = new Scanner(System.in);
        System.out.println("Enter the number of elements you want to enter in the list" );
        int size = ob.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        System.out.println("Enter " + size + " numbers");
        for (int i = 0; i < size; i++)
            arr.add(ob.nextInt());
        Collections.sort(arr);
        System.out.println("Enter the number you wish to find");
        int to_find = ob.nextInt();
        boolean isPresent = binarysearch(arr, to_find);
        if (isPresent)
            System.out.println("Yes the element is present in the list");
        else
            System.out.println("Sorry the element is not present in the list");
        return;
    }
}


    
