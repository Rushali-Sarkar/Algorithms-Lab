import java.util.*;

class Address {

    private String houseNo;
    private String streetNo;
    private String city;
    private String state;
    private String Country;
    private String village;
    private String postOffice;
    private String district;
    private int pinCode;

    Address() {
        this.houseNo = "";
        this.streetNo = "";
        this.city = "";
        this.state = "";
        this.Country = "";
        this.village = "";
        this.postOffice = "";
        this.district = "";
        this.pinCode = 0;
    }

    Address(String houseNo, String streetNo, String city, String state, String Country, String village, String postOffice, String district, int pinCode) {
        this.houseNo = houseNo;
        this.streetNo = streetNo;
        this.city = city;
        this.state = state;
        this.Country = Country;
        this.village = village;
        this.postOffice = postOffice;
        this.district = district;
        this.pinCode = pinCode;
    }

    void eraseData() {
        this.houseNo = "";
        this.streetNo = "";
        this.city = "";
        this.state = "";
        this.Country = "";
        this.village = "";
        this.postOffice = "";
        this.district = "";
        this.pinCode = 0;
        return;
    }

    void reinitialize(String houseNo, String streetNo, String city, String state, String Country, String village, String postOffice, String district, int pinCode) {
        this.houseNo = houseNo;
        this.streetNo = streetNo;
        this.city = city;
        this.state = state;
        this.Country = Country;
        this.village = village;
        this.postOffice = postOffice;
        this.district = district;
        this.pinCode = pinCode;
        return;
    }

    String getHouseNo() {
        return this.houseNo;
    }

    String getStreetNo() {
        return this.streetNo;
    }

    String getCity() {
        return this.city;
    }

    String getState() {
        return this.state;
    }

    String getCountry() {
        return this.Country;
    }

    String getVillage() {
        return this.village;
    }

    String getPostOffice() {
        return this.postOffice;
    }

    String getDistrict() {
        return this.district;
    }

    int getPinCode() {
        return this.pinCode;
    }
}

class Employee extends Address{
    private int empId;
    private String name;
    private Address address;
    private String email;
    private long mobileNo;
    private double sal;

    Employee() {
        this.empId = 0;
        this.name = "";
        this.address = new Address();
        this.email = "";
        this.mobileNo = 0;
        this.sal = 0.0;
    }

    Employee(int empId, String name, String houseNo, String streetNo, String city, String state, String Country, String village, String postOffice, String district, int pinCode, String email, long mobileNo, double sal) {
        this.empId = empId;
        this.name = name;
        this.address = new Address(houseNo, streetNo, city, state, Country, village, postOffice, district, pinCode);
        this.email = email;
        this.mobileNo = mobileNo;
        this.sal = sal;
    }

    void eraseData() {
        this.empId = 0;
        this.name = "";
        this.address = new Address();
        this.email = "";
        this.mobileNo = 0;
        this.sal = 0.0;
        return;
    }

    void reinitialize(int empId, String name, String houseNo, String streetNo, String city, String state, String Country, String village, String postOffice, String district, int pinCode, String email, long mobileNo, double sal) {
        this.empId = empId;
        this.name = name;
        this.address = new Address(houseNo, streetNo, city, state, Country, village, postOffice, district, pinCode);
        this.email = email;
        this.mobileNo = mobileNo;
        this.sal = sal;
        return;
    }

    int getEmpId() {
        return this.empId;
    }

    String getName() {
        return this.name;
    }

    Address getAddress() {
        return this.address;
    }

    String getEmail() {
        return this.email;
    }

    long getMobileNo() {
        return this.mobileNo;
    }

    double getSalary() {
        return this.sal;
    }
}

public class Main {


    private static int totalEmployees;
    private static Employee[] allEmployees;

    public static void printDetails() {
        for (int i = 0; i < totalEmployees; i++) {
            Employee employee = allEmployees[i];
            System.out.format("Employee Id: %d , Employee Name: %s, House Number: %s, Street Number: %s, City: %s, State: %s, Country: %s, Village: %s, Post Office: %s, District: %s, Pin Code: %d, Email Id: %s, Mobile Number: %d, Salary: %f", employee.getEmpId(), employee.getName(), employee.getAddress().getHouseNo(), employee.getAddress().getStreetNo(), employee.getAddress().getCity(), employee.getAddress().getState(), employee.getAddress().getCountry(), employee.getAddress().getVillage(), employee.getAddress().getPostOffice(), employee.getAddress().getDistrict(), employee.getAddress().getPinCode(), employee.getEmail(), employee.getMobileNo(), employee.getSalary());
            System.out.println();
            System.out.println();
        }
        return;
    }

    public static void sortDetails() {
        Arrays.sort(allEmployees, new Comparator < Employee > () {
        public int compare(Employee one, Employee two) {
        if (one.getSalary() > two.getSalary())
            return 1;
        if (one.getSalary() < two.getSalary()) 
            return -1;
        return 0;
        }
        });
        return;
    }

    public static void main (String args[]) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of employees you want to register ?");
        totalEmployees = sc.nextInt();
        allEmployees = new Employee[totalEmployees];
        for (int i = 0; i < totalEmployees; i++) {
            System.out.println("Enter Details of Employee " + (i + 1));
            System.out.println("Enter Employee ID");
            int empId = sc.nextInt();
            System.out.println("Enter Employee Name");
            String name = sc.nextLine();
            String name = sc.nextLine();
            System.out.println("Enter House Number");
            String houseNo = sc.nextLine();
            System.out.println("Enter Street Number");
            String streetNo = sc.nextLine();
            System.out.println("Enter City");
            String city = sc.nextLine();
            System.out.println("Enter State");
            String state = sc.nextLine();
            System.out.println("Enter Country");
            String Country = sc.nextLine();
            System.out.println("Enter Village");
            String village = sc.nextLine();
            System.out.println("Enter Post Office");
            String postOffice = sc.nextLine();
            System.out.println("Enter District");
            String district = sc.nextLine();
            System.out.println("Enter Pin Code");
            int pinCode = sc.nextInt();
            System.out.println("Enter Email");
            String email = sc.nextLine();
            System.out.println("Enter Mobile Number");
            long mobileNo = sc.nextLong();
            System.out.println("Enter Salary");
            double sal = sc.nextDouble();
            Employee employee = new Employee(empId, name, houseNo, streetNo, city, state, Country, village, postOffice, district, pinCode, email, mobileNo, sal);
            allEmployees[i] = employee;
        }
        sc.close(); 
        sortDetails();
        printDetails();
        return;
    }
}