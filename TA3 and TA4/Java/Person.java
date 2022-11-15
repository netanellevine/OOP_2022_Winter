public abstract class Person {
    private final int ID;
    private String firstName;
    private String lastName;
    private String phoneNumber;
    private Address address;
    private Title title;

    public Person(int ID, String firstName, String lastName) {
        this.ID = ID;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public Person(int ID, String firstName, String lastName, String phoneNumber, Address address) {
        this.ID = ID;
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
        this.address = address;
    }

    public int getID() {
        return ID;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public void updateTitle(Title t){
        this.title = t;
    }

    public String getFullName(){
        if (this.title == null){
            return this.firstName + " " + this.lastName;
        }
        return this.title + " " + this.firstName + " " + this.lastName;
    }

    @Override
    public String toString() {
        return "Person {" +
                "ID=" + ID +
                ", fullName='" + getFullName() + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", address=" + address +
                '}';
    }
}
