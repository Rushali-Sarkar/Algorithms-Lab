import java.util.*;

class maximum_minimum {

    public static int maximum;
    public static int minimum;

    public maximum_minimum(int maximum, int minimum) {
        this.maximum = maximum;
        this.minimum = minimum;
    }
}

class maxmin {

    public static void findmaxmin(ArrayList<Integer> arr, maximum_minimum ob, int starting_index, int ending_index) {

        if (arr.size() == 0)
            return;
        
        if (starting_index == ending_index) {

            if (arr.get(starting_index) > ob.maximum) 
                ob.maximum = arr.get(starting_index);
            if (arr.get(starting_index) < ob.minimum)
                ob.minimum = arr.get(starting_index);
            return;
        }

        int middle_index = starting_index + (ending_index - starting_index) / 2;
        findmaxmin(arr, ob, starting_index, middle_index);
        findmaxmin(arr, ob, middle_index + 1, ending_index);
        return;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        maximum_minimum ob = new maximum_minimum(Integer.MIN_VALUE, Integer.MAX_VALUE);

        System.out.println("Enter the number of elements you wish to enter in the array");
        int size = sc.nextInt();
        System.out.println("Enter " + size + " elements");
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < size; i++)
            arr.add(sc.nextInt());
        findmaxmin(arr, ob, 0, size - 1);
        System.out.println("Maximum: " + ob.maximum);
        System.out.println("Minimum: " + ob.minimum);
        return;
    }
}




