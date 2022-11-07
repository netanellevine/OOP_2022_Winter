import java.util.HashMap;

public class Student extends Person {
    private String faculty;
    private String major;
    private int year;
//    private HashMap<Integer, Course> futureCourses;
//    private HashMap<Integer, Course> oldCourses;
//    private HashMap<Integer, Course> currentCourses;
    private HashMap<Integer, Course> courses;
    private static int Index;

    static {
        System.out.println("Student.class is uploaded into JVM");
    }

    {
//        this.futureCourses = new HashMap<>();
//        this.oldCourses = new HashMap<>();
//        this.currentCourses = new HashMap<>();
        this.courses = new HashMap<>();
        Index++;
        System.out.println("New student added, total amount of students -> " + Index);
    }

    public Student(int ID, String firstName, String lastName) {
        super(ID, firstName, lastName);
    }

    public Student(int ID, String firstName, String lastName, String faculty, String major) {
        super(ID, firstName, lastName);
        this.year = 1;
        this.faculty = faculty;
        this.major = major;

    }

    public Student(int ID, String firstName, String lastName, String faculty, String major, String phoneNumber, Address address) {
        super(ID, firstName, lastName, phoneNumber, address);
        this.year = 1;
        this.faculty = faculty;
        this.major = major;
    }

    /**
     * This method purpose is to add course for the courses HashMap of this particular student.
     * @param course - the course to add.
     * @return true if the course was added successfully false otherwise.
     */
    public boolean addCourse(Course course) {
        if (course == null) {
            throw new NullPointerException("Can't add NULL course!");
//            System.err.println("Can't add NULL course!");
//            return false;
        }
        // Already took the course or shouldn't take this course
//        if (!this.futureCourses.containsKey(course.getNumber()) || this.oldCourses.containsKey(course.getNumber()))
//        {
//            return false;
//        }
//        //  Taking the course currently.
//        if (!this.currentCourses.containsKey(course.getNumber()))
//        {
//            this.currentCourses.put(course.getNumber(), course);
//            return true;
//        }
//        return false;
        if (this.courses.containsKey(course.getNumber()))
        {
            System.err.println("This student already enrolled " + course.getName() + " course!");
            return false;
        }
        this.courses.put(course.getNumber(), course);
        return true;
    }


    public String getFaculty() {
        return faculty;
    }

    public void setFaculty(String faculty) {
        this.faculty = faculty;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public HashMap<Integer, Course> getCourses() {
        return courses;
    }


//    public HashMap<Integer, Course> getFutureCourses() {
//        return futureCourses;
//    }


//    public HashMap<Integer, Course> getOldCourses() {
//        return oldCourses;
//    }


//    public HashMap<Integer, Course> getCurrentCourses() {
//        return currentCourses;
//    }



    @Override
    public String toString() {
        return "Student- {" +
                super.toString() +
                ",\nfaculty='" + faculty + '\'' +
                ", major='" + major + '\'' +
                ", year=" + year +
                ",\ncourses=" + courses.values() +
                '}';
    }
}
