import org.junit.jupiter.api.Test;


import static org.junit.jupiter.api.Assertions.*;

class StudentTest {
    Student s1 = new Student(1, "David", "Cohen", "Engineering", "EC", "555", new Address("Ramat-Gan", "Bialik", "55"));
    Student s2 = new Student(2, "David", "Cohen");

    Course OOP1 = new Course(132, "OOP", "Elizabeth");
    Course OOP2 = new Course(123, "OOP", "Natan");
    Course LinearAlgebra2 = new Course(572, "LinearAlgebra2", "Yona");
    Course Algorithms = new Course(5556, "Algorithms", "Gabriel");

    @Test
    void addCourse() {
        assertNotEquals(s1, s2);

        assertTrue(s1.addCourse(OOP1));
        assertTrue(s1.addCourse(LinearAlgebra2));
        assertTrue(s1.addCourse(Algorithms));
        assertFalse(s1.addCourse(OOP1));
        assertThrows(NullPointerException.class, ()->s1.addCourse(null));
//        assertThrows(ArrayIndexOutOfBoundsException.class, ()->s1.addCourse(null));
//        assertTrue(s1.addCourse(Algorithms));

    }
}