public class Address {
    private String city;
    private String street;
    private String number;
    private int floor;
    private String apartment;
    private String postCode;

    boolean shortAddress = false;

    public Address(String city, String street, String number, int floor, String apartment, String postCode) {
        this.city = city;
        this.street = street;
        this.number = number;
        this.floor = floor;
        this.apartment = apartment;
        this.postCode = postCode;
    }

    public Address(String city, String street, String number) {
        this.city = city;
        this.street = street;
        this.number = number;
        this.shortAddress = true;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public String getApartment() {
        return apartment;
    }

    public void setApartment(String apartment) {
        this.apartment = apartment;
    }

    public String getPostCode() {
        return postCode;
    }

    public void setPostCode(String postCode) {
        this.postCode = postCode;
    }

    @Override
    public String toString() {
        if (this.shortAddress){
            return "Address{" +
                    "city='" + city + '\'' +
                    ", street='" + street + '\'' +
                    ", number='" + number + '\'' +
                    '}';
        }
        return "Address{" +
                "city='" + city + '\'' +
                ", street='" + street + '\'' +
                ", number='" + number + '\'' +
                ", floor=" + floor +
                ", apartment='" + apartment + '\'' +
                ", postCode='" + postCode + '\'' +
                '}';
    }
}
