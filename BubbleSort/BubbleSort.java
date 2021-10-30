import java.util.*;

class BubbleSort {

    public static void print(ArrayList<Integer> arr) {
        for (int i = 0; i < arr.size(); i++)
            System.out.print(arr.get(i) + "\t");
        System.out.println();
        return;
    }

    public static ArrayList<Integer> bubblesort(ArrayList<Integer> arr) {
        
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr.get(i) > arr.get(j)) {
                    Integer temp = arr.get(i);
                    arr.set(i, arr.get(j));
                    arr.set(j, temp);
                }
            }
        }
        return arr;
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
        arr = bubblesort(arr);
        System.out.println("The numbers after sorting are");
        print(arr);
        return;
    }
}