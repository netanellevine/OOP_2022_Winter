public class Main {
    public static void main(String[] args) {
//        Title t = Title.Prof;
//        t.printName("Dana");
        Student s1 = new Student(1, "David", "Cohen", "Engineering", "EC", "555", new Address("Ramat-Gan", "Bialik", "55"));
        Student s2 = new Student(2, "David", "Cohen");

        Course OOP1 = new Course(132, "OOP", "Elizabeth");
        Course OOP2 = new Course(123, "OOP", "Natan");
        Course LinearAlgebra2 = new Course(572, "LinearAlgebra2", "Yona");
        Course Algorithms = new Course(5556, "Algorithms", "Gabriel");
        System.out.println("_________________________________________________________________________");
        System.out.println(s1);
        System.out.println("_________________________________________________________________________");
        s1.addCourse(OOP1);
        s1.addCourse(LinearAlgebra2);
        s1.addCourse(Algorithms);
//
//        s1.updateTitle(Title.Dr);
//        s1.updateTitle(t);
        System.out.println("_________________________________________________________________________");
        System.out.println(s1);
        System.out.println("___________________________________________________________________");
//        s1.addCourse(null);
//        System.out.println("BLA");
    }
}