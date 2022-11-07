public class Course {
    private final int number;
    private String name;
    private String lecturer;

    public Course(int number, String name, String lecturer) {
        this.number = number;
        this.name = name;
        this.lecturer = lecturer;
    }

    public int getNumber() {
        return number;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLecturer() {
        return lecturer;
    }

    public void setLecturer(String lecturer) {
        this.lecturer = lecturer;
    }

    @Override
    public String toString() {
        return "Course {" +
                "number=" + number +
                ", name='" + name + '\'' +
                ", lecturer='" + lecturer + '\'' +
                '}';
    }
}
