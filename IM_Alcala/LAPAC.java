// This class represents a student with basic information
public class Student {

    // Attributes (or properties) of a student
    String name;
    int age;
    String major;
    double gpa;

    // Constructor: This method is called when a new Student object is created
    // It sets the initial values for name, age, major, and GPA
    public Student(String name, int age, String major, double gpa) {
        this.name = name;
        this.age = age;
        this.major = major;
        this.gpa = gpa;
    }

    // This method simulates the student studying
    public void study() {
        System.out.println(name + " is studying...");
    }

    // This method displays the student's details
    public void displayInfo() {
        System.out.println("Student Information:");
        System.out.println("---------------------");
        System.out.println("Name : " + name);
        System.out.println("Age  : " + age);
        System.out.println("Major: " + major);
        System.out.println("GPA  : " + gpa);
    }
}
