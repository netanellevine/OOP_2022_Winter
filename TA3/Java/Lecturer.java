public class Lecturer extends Person {
    private int employeeNumber;
    private String faculty;
    private int experience;

    public Lecturer(int ID, String firstName, String lastName) {
        super(ID, firstName, lastName);
    }

    public Lecturer(int ID, String firstName, String lastName, String phoneNumber, Address address) {
        super(ID, firstName, lastName, phoneNumber, address);
    }

    public int getEmployeeNumber() {
        return employeeNumber;
    }


    public String getFaculty() {
        return faculty;
    }

    public void setFaculty(String faculty) {
        this.faculty = faculty;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }
}
