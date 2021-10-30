import java.util.*;

class MatrixOperations {

   private static int n;
   private static int[][] list1;
   private static int[][] list2;
   private static int[][] addedList;
   private static int[][] multipliedList;

   public static void getInput() {
       Scanner sc = new Scanner(System.in);
       System.out.println("Enter the number of rows and columns in matrix");
        n = sc.nextInt();
        list1 = new int[n][n];
        list2 = new int[n][n];
        addedList = new int[n][n];
        multipliedList = new int[n][n];
        System.out.println("Enter Matrix 1");
       for (int i = 0; i < n; i++) {
           for (int j = 0; j < n; j++) {
               list1[i][j] = sc.nextInt();
           }
       }
       System.out.println("Enter Matrix 2");
       for (int i = 0; i < n; i++) {
           for (int j = 0; j < n; j++) {
               list2[i][j] = sc.nextInt();
           }
       }
       sc.close();
       return;
   }

   public static void printList(int[][] list) {
       for (int i = 0; i < n; i++) {
           for (int j = 0; j < n; j++) {
               System.out.print(list[i][j] + "\t");
           }
           System.out.println();
       }
       return;
   }


   public static void addList() {
       for (int i = 0; i < n; i++) {
           for (int j = 0; j < n; j++) {
               addedList[i][j] = list1[i][j] + list2[i][j];
           }
       }
       return;
   }

    public static void multiplyList() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int sum = 0;
                for (int k = 0; k < n; k++) {
                        sum += list1[i][k] * list2[k][j];
                }
                multipliedList[i][j] = sum;
            }
     }
    return;
    }

    public static void main(String args[]) {
       getInput();
       addList();
       multiplyList();
       System.out.println("Added Matrix: ");
       printList(addedList);
       System.out.println("Multiplied Matrix: ");
       printList(multipliedList);
       return;
    }
}