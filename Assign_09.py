// Employee → Manager (Inheritance)
import java.util.Scanner;

class Employee {
    String name;
    int age;
    double salary;
    String address;

    void getInput(Scanner sc) {
        System.out.print("Enter Name: ");
        name = sc.nextLine();

        System.out.print("Enter Age: ");
        age = sc.nextInt();

        System.out.print("Enter Salary: ");
        salary = sc.nextDouble();
        sc.nextLine(); // consume newline

        System.out.print("Enter Address: ");
        address = sc.nextLine();
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Salary: " + salary);
        System.out.println("Address: " + address);
    }
}

class Manager extends Employee {
    String department;

    void getManagerInput(Scanner sc) {
        getInput(sc);
        System.out.print("Enter Department: ");
        department = sc.nextLine();
    }

    void displayManager() {
        display();
        System.out.println("Department: " + department);
        System.out.println("------------------------");
    }
}

public class Main1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Manager[] managers = new Manager[10];

        for (int i = 0; i < 10; i++) {
            System.out.println("\nEnter details of Manager " + (i + 1));
            managers[i] = new Manager();
            managers[i].getManagerInput(sc);
        }

        System.out.println("\n--- Manager Details ---");
        for (int i = 0; i < 10; i++) {
            managers[i].displayManager();
        }

        sc.close();
    }
}
